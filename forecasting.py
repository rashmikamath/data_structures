#from .Objective import Objective
import multiprocessing
from joblib import Parallel, delayed
from tqdm import tqdm
import pandas as pd
import ast
from sklearn.preprocessing import StandardScaler
from sklearn.inspection import permutation_importance
import sklearn.ensemble
import sklearn.model_selection
import sklearn.svm
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from sklearn.compose import TransformedTargetRegressor
import optuna
from sklearn.datasets import load_boston

#from quantile import QuantileTransformer
from optuna.samplers import TPESampler
from sklearn.metrics import make_scorer
import numpy as np
import json
import multiprocessing
from joblib import Parallel, delayed
import datetime
import calendar
import sklearn.preprocessing


class Forecasting():

    def __init__(self,inp_params,category_variable,lag_a,lag_b,feature_lag_a,
                feature_lag_b,cols_to_shift_lag_a,cols_to_shift_lag_b,feature_columns_lag_a,feature_columns_lag_b,
                validation_period,validation_divisions,prediction_period,test_period,evaluation_parameter,data_list,df_best,imp_flag,imp_path,transform_global,target_var,main_df):
        self.inp_params = inp_params
        self.target_var = target_var
        self.category_variable = category_variable
        self.lag_a = lag_a
        self.lag_b = lag_b
        self.feature_lag_a = feature_lag_a
        self.feature_lag_b = feature_lag_b
        self.cols_to_shift_lag_a = cols_to_shift_lag_a
        self.cols_to_shift_lag_b = cols_to_shift_lag_b
        self.feature_columns_lag_a = feature_columns_lag_a
        self.feature_columns_lag_b = feature_columns_lag_b
        self.validation_period = validation_period
        self.validation_divisions = validation_divisions
        self.prediction_period = prediction_period
        self.test_period = test_period
        self.evaluation_parameter = evaluation_parameter
        self.data_list = data_list
        self.df_best = df_best
        self.imp_flag = imp_flag
        self.imp_path = imp_path
        self.transform_global = transform_global
        self.main_df = main_df
    def call_forecasting(self):

        forecasting_output = Parallel(n_jobs=multiprocessing.cpu_count())(delayed(self.forecasting)(df) for df in tqdm(self.data_list))
        #processed_list2 = Parallel(n_jobs=num_cores)(delayed(forecasting)(df) for df in tqdm(data_list))
        importances_output= [sublist[4:] for sublist in forecasting_output]
        df_forecast_output = pd.DataFrame([sublist[:4] for sublist in forecasting_output], columns=['KEY','Date','Actuals','Forecast'])
        df_forecast = self.forecast_from_forecast_output(df_forecast_output)

        if self.imp_flag==1:
            self.write_importances(importances_output)
        df_stat = self.stat_create(self.main_df)
        df_forecast_final = self.forecast_correction(df_forecast,df_stat)
        return df_forecast_final

    def stat_create(self,main_df):
        df_stat = main_df.loc[main_df['Year']<datetime.datetime.now().year].groupby(['Depot', 'Used_channel', 'SPGR','Quarter']).agg({'QUANTITY':['min','max']}).reset_index()
        df_stat.columns = ['Depot', 'Used_channel', 'SPGR','Quarter','Min_quantity','Max_quantity']
        return df_stat

    def forecast_correction(self,df_forecast,df_stat):
        df_forecast_final = pd.merge(df_forecast[['Date', 'Forecast', 'Depot', 'Channel', 'BGR','SPGR','Quarter']],
                                                    df_stat,how='left',left_on=['Depot', 'Channel','SPGR','Quarter'],
                                                    right_on= ['Depot', 'Used_channel', 'SPGR', 'Quarter'],validate='m:1')
        df_forecast_final['Forecast'] = np.where(df_forecast_final['Forecast'] >df_forecast_final['Max_quantity']*1.2, df_forecast_final['Max_quantity']*1.2, df_forecast_final['Forecast'])
        return df_forecast_final

    def write_importances(self,importances_output):
        df_imp_output = pd.DataFrame(importances_output, columns = ['KEY','cols','imp_mean','imp_std'])
        df_importances = pd.DataFrame()
        for key in df_imp_output.KEY.unique():
            df_sub = df_imp_output[df_imp_output.KEY==key].copy()
            df_temp = pd.DataFrame({'key':key,'columns':df_sub['cols'].values[0],'imp_mean':df_sub['imp_mean'].values[0].tolist(),'imp_std':df_sub['imp_std'].values[0].tolist()})
            df_importances = pd.concat([df_importances,df_temp],axis=0)
        df_importances.to_csv(self.imp_path+'/monthly_importances.csv',index = False)

    def forecast_from_forecast_output(self,df_forecast_output):
        df_forecast =pd.DataFrame()
        for key in df_forecast_output.KEY.unique():
            df_sub = df_forecast_output[df_forecast_output.KEY==key].copy()
            df_temp = pd.DataFrame({'key':key,'Date':df_sub['Date'].values[0].tolist(),'Forecast':df_sub['Forecast'].values[0].tolist()})
            #print(df_sub['Forecast'].values[0].ravel())
            df_forecast = pd.concat([df_forecast,df_temp],axis=0)
        df_forecast[['Depot','BGR','SPGR','Channel']] = df_forecast.key.str.split(pat='|',expand=True)
        df_forecast['Quarter'] = pd.to_datetime(df_forecast['Date']).dt.quarter
        df_forecast['SPGR'] = df_forecast['SPGR'].astype(str)
        return df_forecast


    def forecasting(self,df):

        # splitting the dataframe into the test train data divisions
        
        df[self.cols_to_shift_lag_a] = df[self.cols_to_shift_lag_a].shift(self.lag_a)
        df[self.cols_to_shift_lag_b] = df[self.cols_to_shift_lag_b].shift(self.lag_b)
        if len(self.feature_lag_a)>0:

            for lag in self.feature_lag_a:
                try:
                    df[[s  +'lag'+str(lag) for s in self.feature_columns_lag_a]] = df[self.feature_columns_lag_a].shift(lag)
                except Exception as e:
                    raise e
        if len(self.feature_lag_b)>0:

            for lag in self.feature_lag_b:
                df[[s  +'lag'+str(lag) for s in self.feature_columns_lag_b]] = df[self.feature_columns_lag_b].shift(lag)
        
        df.dropna(inplace = True)

        unique_key=df['key'].iloc[0] #defining the unique id for the 

        print('running forecasting for ',unique_key)

        best_params = self.df_best.loc[self.df_best['KEY']==unique_key]['Params'].values[0]
        best_params = ast.literal_eval(best_params)
        #print('Best_params  ##',best_params)
        try:
            df,y_pred,regressor_obj,cols,imp_mean,imp_std = self.model_from_params(df,best_params,self.imp_flag)
        except Exception as e:
            raise e
            print(e)
            df,y_pred,regressor_obj,cols,imp_mean,imp_std = df, np.zeros(self.prediction_period), "None",0,0,0
        date = df.index[-self.prediction_period:]
        actual = df[self.target_var][-self.prediction_period:]
        return [unique_key,date,actual,y_pred,unique_key,cols,imp_mean,imp_std]


    def model_from_params(self,main_df,params,imp_flag):
    
    
        main_df = main_df.drop(columns=['key'])
        #print('dtype', type(params))
        regressor_name = params['regressor']
        df = main_df.copy()
        df=df.drop(columns=self.category_variable)
        
        if regressor_name == 'SVR':

            svc_c = params['svc_c']

            svc_kernel = params['svc_kernel']
            svc_degree = params['svc_degree']
            svc_gamma = params['svc_gamma']
            svc_epsilon = params['svc_epsilon']
            svc_max_iter = params['svc_max_iter']
            if self.transform_global=='tune':
                transformer_type = params['transformer_type']
            else:
                transformer_type = self.transform_global


            if(transformer_type=='Quantile'):
                regressor_obj = TransformedTargetRegressor(regressor=sklearn.svm.SVR(C=svc_c, kernel = svc_kernel,degree=svc_degree,gamma=svc_gamma,
                                    epsilon = svc_epsilon,max_iter = svc_max_iter),transformer=QuantileTransformer(n_quantiles=5, output_distribution='uniform', ignore_implicit_zeros=False, subsample=1000, random_state=3, copy=True),check_inverse=False)

            if(transformer_type=='Power'):
                regressor_obj = TransformedTargetRegressor(regressor=sklearn.svm.SVR(C=svc_c, kernel = svc_kernel,degree=svc_degree,gamma=svc_gamma,
                                epsilon = svc_epsilon,max_iter = svc_max_iter),transformer=PowerTransformer(),check_inverse=False)

            if(transformer_type=='log1p'):
                regressor_obj = TransformedTargetRegressor(regressor=sklearn.svm.SVR(C=svc_c, kernel = svc_kernel,degree=svc_degree,gamma=svc_gamma,
                                epsilon = svc_epsilon,max_iter = svc_max_iter),func=np.log1p,inverse_func=np.expm1,check_inverse=False)
                        
            else:
                regressor_obj = TransformedTargetRegressor(regressor=sklearn.svm.SVR(C=svc_c, kernel = svc_kernel,degree=svc_degree,gamma=svc_gamma,
                                epsilon = svc_epsilon,max_iter = svc_max_iter),transformer=None,check_inverse=False)



            


        elif regressor_name == 'RandomForest':

            rf_max_depth = params['rf_max_depth']
            rf_n_estimators = params['rf_n_estimators']
            rf_min_samples_split = params['rf_min_samples_split']
            rf_min_samples_leaf = params['rf_n_estimators']
            rf_max_features = params['rf_max_features']
            # rf_bootstrap  = params['rf_bootstrap']
            # rf_oob_score  = params['rf_oob_score']
            if self.transform_global=='tune':
                transformer_type = params['transformer_type']
            else:
                transformer_type = self.transform_global

            if(transformer_type=='Power'):


                regressor_obj = TransformedTargetRegressor(regressor=sklearn.ensemble.RandomForestRegressor(max_depth=rf_max_depth, n_estimators=rf_n_estimators,
                                                min_samples_split=rf_min_samples_split,min_samples_leaf=rf_min_samples_leaf,max_features = rf_max_features,
                                                random_state=3),transformer=PowerTransformer(),check_inverse=False)
            
            if(transformer_type=='Quantile'):


                regressor_obj = TransformedTargetRegressor(regressor=sklearn.ensemble.RandomForestRegressor(max_depth=rf_max_depth, n_estimators=rf_n_estimators,
                                                min_samples_split=rf_min_samples_split,min_samples_leaf=rf_min_samples_leaf,max_features = rf_max_features,
                                                random_state=3),transformer=QuantileTransformer(n_quantiles=5, output_distribution='uniform', ignore_implicit_zeros=False, subsample=1000, random_state=3, copy=True),check_inverse=False)
            
            if(transformer_type=='log1p'):


                regressor_obj = TransformedTargetRegressor(regressor=sklearn.ensemble.RandomForestRegressor(max_depth=rf_max_depth, n_estimators=rf_n_estimators,
                                                min_samples_split=rf_min_samples_split,min_samples_leaf=rf_min_samples_leaf,max_features = rf_max_features,
                                                random_state=3),func=np.log1p,inverse_func=np.expm1,check_inverse=False)
            
            else:


                regressor_obj = TransformedTargetRegressor(regressor=sklearn.ensemble.RandomForestRegressor(max_depth=rf_max_depth, n_estimators=rf_n_estimators,
                                                min_samples_split=rf_min_samples_split,min_samples_leaf=rf_min_samples_leaf,max_features = rf_max_features,
                                                random_state=3),transformer=None,check_inverse=False)

        elif regressor_name=='XGboost' :

            xg_n_estimators = params['xg_n_estimators']
            xg_max_depth = params['xg_max_depth']
            xg_learning_rate = params['xg_learning_rate']
            xg_booster = params['xg_booster']
            xg_subsample = params['xg_subsample']
            xg_colsample_bytree = params['xg_colsample_bytree']
            xg_colsample_bylevel = params['xg_colsample_bylevel']
            xg_colsample_bynode = params['xg_colsample_bynode']
            xg_reg_alpha = params['xg_reg_alpha']
            xg_reg_lambda = params['xg_reg_lambda']
            xg_gamma = params['xg_gamma']
            xg_min_child_weight  = params['xg_min_child_weight']
            if self.transform_global=='tune':
                transformer_type = params['transformer_type']
            else:
                transformer_type = self.transform_global


            if(transformer_type=='Quantile'):

                regressor_obj = TransformedTargetRegressor(regressor=XGBRegressor(max_depth=xg_max_depth, learning_rate=xg_learning_rate, n_estimators=xg_n_estimators,booster=xg_booster,
                                                            subsample = xg_subsample,colsample_bytree = xg_colsample_bytree,colsample_bylevel=xg_colsample_bylevel,
                                                            colsample_bynode=xg_colsample_bynode,reg_alpha= xg_reg_alpha,reg_lambda=xg_reg_lambda,
                                                            gamma = xg_gamma,min_child_weight=xg_min_child_weight),transformer=QuantileTransformer(n_quantiles=5, output_distribution='uniform', ignore_implicit_zeros=False, subsample=1000, random_state=3, copy=True),
                                            check_inverse=False)
            if(transformer_type=='log1p'):

                regressor_obj = TransformedTargetRegressor(regressor=XGBRegressor(max_depth=xg_max_depth, learning_rate=xg_learning_rate, n_estimators=xg_n_estimators,booster=xg_booster,
                                                            subsample = xg_subsample,colsample_bytree = xg_colsample_bytree,colsample_bylevel=xg_colsample_bylevel,
                                                            colsample_bynode=xg_colsample_bynode,reg_alpha= xg_reg_alpha,reg_lambda=xg_reg_lambda,
                                                            gamma = xg_gamma,min_child_weight=xg_min_child_weight),func=np.log1p,inverse_func=np.expm1,
                                            check_inverse=False)
            if(transformer_type=='Power'):

                regressor_obj = TransformedTargetRegressor(regressor=XGBRegressor(max_depth=xg_max_depth, learning_rate=xg_learning_rate, n_estimators=xg_n_estimators,booster=xg_booster,
                                                            subsample = xg_subsample,colsample_bytree = xg_colsample_bytree,colsample_bylevel=xg_colsample_bylevel,
                                                            colsample_bynode=xg_colsample_bynode,reg_alpha= xg_reg_alpha,reg_lambda=xg_reg_lambda,
                                                            gamma = xg_gamma,min_child_weight=xg_min_child_weight),transformer=PowerTransformer(),
                                            check_inverse=False)
            else:

                regressor_obj = TransformedTargetRegressor(regressor=XGBRegressor(max_depth=xg_max_depth, learning_rate=xg_learning_rate, n_estimators=xg_n_estimators,booster=xg_booster,
                                                            subsample = xg_subsample,colsample_bytree = xg_colsample_bytree,colsample_bylevel=xg_colsample_bylevel,
                                                            colsample_bynode=xg_colsample_bynode,reg_alpha= xg_reg_alpha,reg_lambda=xg_reg_lambda,
                                                            gamma = xg_gamma,min_child_weight=xg_min_child_weight),transformer=None,
                                            check_inverse=False)
        
        elif regressor_name == 'lightgbm':

            lgbm_boosting_type = params['lgbm_boosting_type']
            
            lgbm_num_leaves = params['lgbm_num_leaves']

            lgbm_max_depth = params['lgbm_max_depth']

            lgbm_learning_rate = params['lgbm_learning_rate']
            lgbm_n_estimators = params['lgbm_n_estimators']

            #lgbm_min_split_gain=0.0 

            lgbm_min_child_weight=params['lgbm_min_child_weight']
            lgbm_min_child_samples=params['']

            #lgbm_subsample=1.0, 
            #lgbm_subsample_freq=0, 
            lgbm_colsample_bytree=params['lgbm_colsample_bytree']
            lgbm_reg_alpha=params['lgbm_reg_alpha']
            lgbm_reg_lambda=params['lgbm_reg_lambda']


            if self.transform_global =='tune':
                transformer_type = params['transformer_type']
            else:

                transformer_type=self.transform_global

            if(transformer_type=='Quantile'):

                regressor_obj = TransformedTargetRegressor(regressor=LGBMRegressor(boosting_type=lgbm_boosting_type, num_leaves=lgbm_num_leaves, max_depth=lgbm_max_depth, learning_rate=lgbm_learning_rate, n_estimators=lgbm_n_estimators,min_child_weight=lgbm_min_child_weight, min_child_samples=lgbm_min_child_samples, 
                                                                                    colsample_bytree=lgbm_colsample_bytree, reg_alpha=lgbm_reg_alpha, reg_lambda=lgbm_reg_lambda, random_state=3),transformer=QuantileTransformer(n_quantiles=5, 
                                                                                    output_distribution='uniform', ignore_implicit_zeros=False, subsample=1000, random_state=3, copy=True),
                                            check_inverse=False)
            if(transformer_type=='log1p'):

                regressor_obj = TransformedTargetRegressor(regressor=LGBMRegressor(boosting_type=lgbm_boosting_type, num_leaves=lgbm_num_leaves, max_depth=lgbm_max_depth, learning_rate=lgbm_learning_rate, n_estimators=lgbm_n_estimators,min_child_weight=lgbm_min_child_weight, min_child_samples=lgbm_min_child_samples, 
                                                                                    colsample_bytree=lgbm_colsample_bytree, reg_alpha=lgbm_reg_alpha, reg_lambda=lgbm_reg_lambda, random_state=3),func=np.log1p,inverse_func=np.expm1,
                                            check_inverse=False)
            if(transformer_type=='Power'):

                regressor_obj = TransformedTargetRegressor(regressor=LGBMRegressor(boosting_type=lgbm_boosting_type, num_leaves=lgbm_num_leaves, max_depth=lgbm_max_depth, learning_rate=lgbm_learning_rate, n_estimators=lgbm_n_estimators,min_child_weight=lgbm_min_child_weight, min_child_samples=lgbm_min_child_samples, 
                                                                                    colsample_bytree=lgbm_colsample_bytree, reg_alpha=lgbm_reg_alpha, reg_lambda=lgbm_reg_lambda, random_state=3),transformer=PowerTransformer(),
                                            check_inverse=False)
            else:

                regressor_obj = TransformedTargetRegressor(regressor=LGBMRegressor(boosting_type=lgbm_boosting_type, num_leaves=lgbm_num_leaves, max_depth=lgbm_max_depth, learning_rate=lgbm_learning_rate, n_estimators=lgbm_n_estimators,min_child_weight=lgbm_min_child_weight, min_child_samples=lgbm_min_child_samples, 
                                                                                    colsample_bytree=lgbm_colsample_bytree, reg_alpha=lgbm_reg_alpha, reg_lambda=lgbm_reg_lambda, random_state=3),transformer=None,
                                            check_inverse=False)

        
        X_train,X_val = df.drop(columns = [self.target_var])[:-self.prediction_period],  df.drop(columns = [self.target_var])[-self.prediction_period:]    
        #print(X_train)
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_val = scaler.transform(X_val)
        y_train = df[self.target_var][:-self.prediction_period]
        
        try:
            #print(regressor_obj.get_params)
            regressor_obj.fit(X_train, y_train.values)

            y_pred = regressor_obj.predict(X_val)
            
        except Exception as e:
            raise e
            # print('#################################################################################',e)
            # print(X_val)
            # print(X_train)
        y_pred = y_pred.clip(min=0)
        
        if (y_pred[0]==np.inf or y_pred[0]==-np.inf or y_pred[0]== 'inf' or y_pred[0]=='-inf' or y_pred[0]==np.nan):
            y_pred = np.zeros(self.prediction_period)
        #print(y_pred)
        if imp_flag==1:
            result = permutation_importance(regressor_obj, X_train, y_train, n_repeats=5,random_state=3)
            cols = df.drop(columns = [self.target_var]).columns.values.tolist()
            imp_mean = result.importances_mean
            imp_std = result.importances_std
            return df,y_pred,regressor_obj,cols,imp_mean,imp_std
            

        else:
            return df,y_pred,regressor_obj,0,0,0

