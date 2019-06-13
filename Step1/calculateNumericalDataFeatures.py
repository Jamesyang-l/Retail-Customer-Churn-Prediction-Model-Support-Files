# The script MUST contain a function named azureml_main
# which is the entry point for this module.
#
###
# Calculate features for the complete timespan of the data
###

import pandas as pd
import numpy as np
from RetailChurnTemplateUtility import *

# The entry point function can contain up to two input arguments:
#   Param<dataframe1>: Joined Activity User Info data without the churn period activity
#   Param<dataframe2>: Features List Dataset
def azureml_main(dataframe1 = None, dataframe2 = None):
    key_column='UserId'
    IsDevelopment=True

    #specifying churn start period
    churn_period=dataframe1.iloc[0]['ChurnPeriod']   

    #       Feature Engineering
    
    churnUtil=RetailChurnTemplateUtility(churn_period=churn_period)
    #       Feature Engineering
    dataframe2=churnUtil.calculateNumericalDataFeatures(dataframe1,key_column, 
                 summable_columns=dataframe1.columns,
                        rename_label='overall', IsDevelopment=IsDevelopment)
    
    return dataframe2
# 
