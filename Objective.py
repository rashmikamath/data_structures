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
import pandas as pd
import json
import multiprocessing
from joblib import Parallel, delayed
import datetime
import calendar
import sklearn.preprocessing

class Objective():

    def __init__(self, inp_params , df):
        #self.study=study
        self.inp_params = inp_params
        self.df = df
        self.target_var =inp_params['Target_Variable'] #the target variable that needs to be predicted 
        self.date_var = inp_params['Date_Variable']  #the variable that contains the date
        self.validation_period = inp_params['Validation_Period'] #the period that needs to be used for the validation
        self.validation_divisions = inp_params['Validation_Divisions'] #total divisions for the validation
        self.prediction_period = inp_params['Prediction_Period'] # the future values that would be predicted 
        self.category_variable = inp_params['Category_Variable'] # list of category variables based on which the unique id for each combination is created
        self.test_period=inp_params['Test_Period']
        self.evaluation_parameter=inp_params['Evaluation_Parameter']
        self.transform_global = inp_params['transform_global']

    def add2(self,x):
        
        return x+200
    
    def sub2(self,x):
        
        return x-200
    
    def mape(self,y_true,y_pred):
    
        return np.divide(np.sum(np.abs(y_true-y_pred)), np.sum(np.abs(y_true+1e-8)))
    
    def accuracy(self,y_true,y_pred):
    
        return 1-np.divide(np.sum(np.abs(y_true-y_pred)), np.sum(np.abs(y_true+1e-8)))

    def __call__(self, trial):
        
        X = self.df.drop(columns = [self.target_var])
        y = self.df[self.target_var]



        regressor_name = trial.suggest_categorical('regressor', ['SVR', 'RandomForest','XGboost'])

        if regressor_name == 'SVR':
            
            if self.transform_global =='tune':
                transformer_type = trial.suggest_categorical('transformer_type',['Quantile','Power','log1p','no_transform'])
            else:

                transformer_type=self.transform_global
            svc_c = trial.suggest_loguniform('svc_c', 1e-3, 1e3)

            svc_kernel = trial.suggest_categorical('svc_kernel',['linear', 'poly', 'rbf'])

            svc_degree = int(trial.suggest_int('svc_degree',2,5))

            svc_gamma = trial.suggest_categorical('svc_gamma',['scale','auto'])

            svc_epsilon = float(trial.suggest_uniform('svc_epsilon',1e-2,1e2))

            svc_max_iter = int(trial.suggest_int('svc_max_iter',5000,20000))

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

            rf_max_depth = int(trial.suggest_int('rf_max_depth', 2, 8))

            rf_n_estimators = int(trial.suggest_int('rf_n_estimators', 50, 150))

            rf_min_samples_split = int(trial.suggest_int('rf_min_samples_split', 2, 5))

            rf_min_samples_leaf = int(trial.suggest_int('rf_min_samples_leaf', 2, 5))

            rf_max_features = trial.suggest_categorical('rf_max_features',[0.5,0.6,0.7,0.8,0.9,1])

            #rf_bootstrap  = trial.suggest_categorical('rf_bootstrap',[1,0])

            #rf_oob_score  = trial.suggest_categorical('rf_oob_score',[1,0])

            if self.transform_global =='tune':
                transformer_type = trial.suggest_categorical('transformer_type',['Quantile','Power','log1p','no_transform'])
            else:

                transformer_type=self.transform_global
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

        elif regressor_name == 'XGboost':

            xg_n_estimators = int(trial.suggest_int('xg_n_estimators', 50, 250))

            xg_max_depth = int(trial.suggest_int('xg_max_depth', 2, 8))

            xg_learning_rate = trial.suggest_loguniform('xg_learning_rate', 1e-2, 1e2)

            xg_booster = trial.suggest_categorical('xg_booster',['gbtree', 'gblinear' ,'dart'])

            xg_subsample = trial.suggest_uniform('xg_subsample',0.7,1.0)

            xg_colsample_bytree = trial.suggest_uniform('xg_colsample_bytree',0.5,1.0)

            xg_colsample_bylevel = trial.suggest_uniform('xg_colsample_bylevel',0.5,1.0)

            xg_colsample_bynode = trial.suggest_uniform('xg_colsample_bynode',0.5,1.0)

            xg_reg_alpha = trial.suggest_uniform('xg_reg_alpha',0.0,1.0)

            xg_reg_lambda = trial.suggest_uniform('xg_reg_lambda',1.0,5.0)

            xg_gamma = trial.suggest_uniform('xg_gamma',1e-2,2.0)

            xg_min_child_weight  = trial.suggest_int('xg_min_child_weight',1,7)

            if self.transform_global =='tune':
                transformer_type = trial.suggest_categorical('transformer_type',['Quantile','Power','log1p','no_transform'])
            else:

                transformer_type=self.transform_global

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

            lgbm_boosting_type = trial.suggest_categorical('lgbm_boosting_type',['gbdt', 'dart' ,'goss'])
            
            

            lgbm_max_depth = int(trial.suggest_int('lgbm_max_depth', 3,8))
            lgbm_num_leaves = int(trial.suggest_int('lgbm_num_leaves', 5,2**lgbm_max_depth))
            lgbm_learning_rate = trial.suggest_loguniform('lgbm_learning_rate', 1e-2, 1e2)

            lgbm_n_estimators = int(trial.suggest_int('lgbm_n_estimators', 50, 250))

            #lgbm_min_split_gain=0.0 

            lgbm_min_child_weight=trial.suggest_loguniform('lgbm_min_child_weight', 1e-2, 3e-2)
            lgbm_min_child_samples=int(trial.suggest_int('lgbm_min_child_samples', 1, 10))

            #lgbm_subsample=1.0, 
            #lgbm_subsample_freq=0, 
            lgbm_colsample_bytree=trial.suggest_uniform('lgbm_colsample_bytree',0.5,1.0)

            lgbm_reg_alpha=trial.suggest_uniform('lgbm_reg_alpha',0.0,1.0)

            lgbm_reg_lambda=trial.suggest_uniform('xg_reg_lambda',1.0,5.0)


            if self.transform_global =='tune':
                transformer_type = trial.suggest_categorical('transformer_type',['Quantile','Power','log1p','no_transform'])
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


        metric_sum = []
        for i in range(self.validation_divisions):
            if i==0:
                X_train, X_val = X[:-(i+1)*self.validation_period] , X[-(i+1)*self.validation_period:] 
                y_train, y_val = y[:-(i+1)*self.validation_period] , y[-(i+1)*self.validation_period:]
                
            else:
                X_train, X_val = X[:-(i+1)*self.validation_period] , X[-(i+1)*self.validation_period:-(i+1)*self.validation_period+self.validation_period] 
                y_train, y_val = y[:-(i+1)*self.validation_period] , y[-(i+1)*self.validation_period:-(i+1)*self.validation_period+self.validation_period]
                
            #print(X_train.shape,X_val.shape,y_train.shape,y_val.shape)
            try:
                scaler = StandardScaler()
                X_train = scaler.fit_transform(X_train)
                X_val = scaler.transform(X_val)
                regressor_obj.fit(X_train, y_train.values)

                y_pred = regressor_obj.predict(X_val)
                #print(y_pred,y_val)
                if self.evaluation_parameter == 'MAPE':

                    metric = self.mape(y_val.values,y_pred)

                elif self.evaluation_parameter == 'Accuracy':

                    metric = self.accuracy(y_val.values,y_pred)

            except Exception as e:
                raise e
                # print('Caught Exception in val div',str(i), e)
                # print('NA in Xtrain' ,np.isnan(np.sum(X_train)))
                # print('NA in Xval' ,np.isnan(np.sum(X_val)))
                # print(X_val)
                # print(X_train)
                #raise e
                if self.evaluation_parameter == 'MAPE':

                    metric = np.inf

                else:

                    metric = -np.inf
                continue
            
            metric_sum.append(metric)

        if len(metric_sum) == 0:
            metric_avg = -np.inf
        else:
            metric_avg = sum(metric_sum)/len(metric_sum)
                
        return metric_avg
