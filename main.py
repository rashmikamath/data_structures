import sys
#A.1.1 insert the path where Multivariate_modelling Package is there 
sys.path.insert(0,'/home/vmadmin/mycontainer/piyush-dev/DSP_Nivea/CodeBase/02_Training/')
#A.1.2 import all the classes from Multivariate_Modelling Package
from Multivariate_Modelling.modelling_pipeline import *

#A.1.3 Call the function of Multivariate_Modelling/modelling_pipeline Class to run the modelling pipeline
#Function : Runs the respective pipeline and saves -
##Forecast results to to the location specified in input_config.py file, key :"forecast_path"
##Feature importances using permutation importance to the location specified in input_config.py file, key :"importance_path"
##best df containing best model's parameters to the location specified in input_config.py file, key : "df_best_path" 
##All other details/inputs as specified in input_config file

run_model_pipeline()
run_forecast_pipeline()
run_model_and_forecast_pipeline()
#go to A.1.3.1 (present in Multivariate_Modelling/modelling_pipeline