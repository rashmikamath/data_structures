from .Config_and_data_load import ConfigDataLoad
import input_config
from .model_training import Train_models
from .forecasting import Forecasting
import multiprocessing
import pandas as pd

date_var = input_config.config_dict['Date_Variable']
target_var = input_config.config_dict['Target_Variable']
file_path = input_config.config_dict['Input_File']
category_variable = input_config.config_dict['Category_Variable']
data_list = []
lag_a = input_config.config_dict['lag_a'] #to be taken from config
lag_b = input_config.config_dict['lag_b'] #to be taken from config
feature_lag_a = input_config.config_dict['feature_lag_a']
feature_lag_b = input_config.config_dict['feature_lag_b']
cols_to_shift_lag_a = input_config.config_dict['cols_to_shift_lag_a'] #to be taken from config
cols_to_shift_lag_b = input_config.config_dict['cols_to_shift_lag_b']
feature_columns_lag_a = input_config.config_dict['feature_columns_lag_a']
feature_columns_lag_b = input_config.config_dict['feature_columns_lag_b']
validation_period = input_config.config_dict['Validation_Period'] #the period that needs to be used for the validation
validation_divisions = input_config.config_dict['Validation_Divisions'] #total divisions for the validation
prediction_period = input_config.config_dict['Prediction_Period'] # the future values that would be predicted 
test_period = input_config.config_dict['Test_Period']
evaluation_parameter = input_config.config_dict['Evaluation_Parameter']
df_best_path = input_config.config_dict['df_best_path']
imp_flag = input_config.config_dict['importance_flag']
imp_path = input_config.config_dict['importance_path']
forecast_path = input_config.config_dict['forecast_path']
transform_global = input_config.config_dict['transform_global']
# num_cores = multiprocessing.cpu_count()
df_best = pd.DataFrame()
main_df = pd.DataFrame()
#A.1.3.2 Function to initialize the object of ConfigDataLoad Class and call its preprocessing function
def data_load_pipe():
    Data_load_obj = ConfigDataLoad(date_var,target_var,file_path,category_variable)
    main_df,data_list = Data_load_obj.call_data_load_preprocessing()
    #print(data_list)
    return main_df,data_list

def training_pipe(main_df,data_list):
    
    feature_columns_lag_a=input_config.config_dict['feature_columns_lag_a']
    col_promo =  [col for col in main_df if col.startswith('Promo')]
    feature_columns_lag_a_full = feature_columns_lag_a + col_promo
    #print(feature_columns_lag_a_extended)
    train_model_obj = Train_models(input_config.config_dict,category_variable,lag_a,lag_b,feature_lag_a,
                feature_lag_b,cols_to_shift_lag_a,cols_to_shift_lag_b,feature_columns_lag_a_full,feature_columns_lag_b,
                validation_period,validation_divisions,prediction_period,test_period,evaluation_parameter,data_list)
    df_best = train_model_obj.call_training()
    df_best.to_csv(df_best_path+"/df_best.csv",index=False)
    return df_best

def forecast_pipe(main_df,data_list):

    feature_columns_lag_a=input_config.config_dict['feature_columns_lag_a']
    col_promo =  [col for col in main_df if col.startswith('Promo')]
    feature_columns_lag_a_full=feature_columns_lag_a + col_promo

    df_best = pd.read_csv(df_best_path+"/df_best.csv")

    forecast_model_obj = Forecasting(input_config.config_dict,category_variable,lag_a,lag_b,feature_lag_a,
                feature_lag_b,cols_to_shift_lag_a,cols_to_shift_lag_b,feature_columns_lag_a_full,feature_columns_lag_b,
                validation_period,validation_divisions,prediction_period,test_period,evaluation_parameter,data_list,df_best,imp_flag,imp_path,transform_global,target_var,main_df)

    df_forecast_final = forecast_model_obj.call_forecasting()
    df_forecast_final.to_csv(forecast_path+"/Monthly_forecast.csv",index=False)
    return df_forecast_final
#A.1.3.1
def run_model_pipeline():
    #A.1.3.1.1 Calls the data_load pipe() which returns main_df(single exhaustive dataframe treated by data_load_preprocessing()
    #function of ConfigDataLoad class imported above) and data_list(a list of dataframes traeted by category_div() function of ConfigDataLoad class imported above)
    try:
        main_df,data_list = data_load_pipe()
        #A.1.3.1.2 Calls the training pipe function which takes main_df and data list returned by data_load_pipe() 
        training_pipe(main_df,data_list)
    # try:
    #     forecast_pipe(main_df,data_list)
    except Exception as e:
        raise e
def run_forecast_pipeline():
    #A.1.3.1.1 Calls the data_load pipe() which returns main_df(single exhaustive dataframe treated by data_load_preprocessing()
    #function of ConfigDataLoad class imported above) and data_list(a list of dataframes traeted by category_div() function of ConfigDataLoad class imported above)
    try:
        main_df,data_list = data_load_pipe()
    #A.1.3.1.2 Calls the training pipe function which takes main_df and data list returned by data_load_pipe() 
    #training_pipe(main_df,data_list)
    
        forecast_pipe(main_df,data_list)
    except Exception as e:
        raise e

def run_model_and_forecast_pipeline():
    #A.1.3.1.1 Calls the data_load pipe() which returns main_df(single exhaustive dataframe treated by data_load_preprocessing()
    #function of ConfigDataLoad class imported above) and data_list(a list of dataframes traeted by category_div() function of ConfigDataLoad class imported above)
    try:
        main_df,data_list = data_load_pipe()
        #A.1.3.1.2 Calls the training pipe function which takes main_df and data list returned by data_load_pipe() 
        training_pipe(main_df,data_list)
    
        forecast_pipe(main_df,data_list)
    except Exception as e:
        raise e