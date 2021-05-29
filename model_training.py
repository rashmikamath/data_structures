from .Objective import Objective
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

class Train_models():

    def __init__(self,inp_params,category_variable,lag_a,lag_b,feature_lag_a,
                feature_lag_b,cols_to_shift_lag_a,cols_to_shift_lag_b,feature_columns_lag_a,feature_columns_lag_b,
                validation_period,validation_divisions,prediction_period,test_period,evaluation_parameter,data_list):
        self.inp_params = inp_params
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
        

    def call_training(self):

        training_output = Parallel(n_jobs=multiprocessing.cpu_count())(delayed(self.training)(df) for df in tqdm(self.data_list))
        df_best = pd.DataFrame(training_output, columns=['KEY','Params', 'Metric'])
        #print('df_best',df_best)
        df_best[['Depot','BGR','SPGR','Channel']] = df_best.KEY.str.split(pat='|',expand=True)
        return df_best



    def training(self,df):

        # splitting the dataframe into the test train data divisions
        
        df[self.cols_to_shift_lag_a] = df[self.cols_to_shift_lag_a].shift(self.lag_a)
        df[self.cols_to_shift_lag_b] = df[self.cols_to_shift_lag_b].shift(self.lag_b)
        if len(self.feature_lag_a)>0:

            for lag in self.feature_lag_a:
                df[[s  +'lag'+str(lag) for s in self.feature_columns_lag_a]] = df[self.feature_columns_lag_a].shift(lag)
        if len(self.feature_lag_b)>0:

            for lag in self.feature_lag_b:
                df[[s  +'lag'+str(lag) for s in self.feature_columns_lag_b]] = df[self.feature_columns_lag_b].shift(lag)
        
        df.dropna(inplace = True)
        df_test = df[-self.test_period:]
        df_train = df[0:-self.test_period]
        #df_full = df.copy()# df_full will be used for prediction
        df = df_train  # df is the main dataframe that is used for the training

        unique_key=df['key'].iloc[0] #defining the unique id for the 

        print('running for',unique_key)
        #removing unnecessary columns
        df=df.drop(columns=self.category_variable)
        #print(df.columns)
        df=df.drop(columns=['key'])


        objective = Objective(self.inp_params,df)

        sampler = TPESampler(**TPESampler.hyperopt_parameters(),seed=3)

        if self.evaluation_parameter == 'MAPE':

            study = optuna.create_study(sampler = sampler,direction='minimize')

        else:

            study = optuna.create_study(sampler = sampler,direction='maximize')
        #take user unput n_trials
        study.optimize(objective, n_trials=200)
        # unique_keys.append(unique_key)
        # best_trials.append(study.best_params)
        # best_metrics.append(study.best_value)
        return [unique_key,study.best_params, study.best_value]
