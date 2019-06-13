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

    #       Feature Engineering
    churnUtil=RetailChurnTemplateUtility()
    df=churnUtil.calculateAverages(dataframe1,dataframe2,
        key_column, uniquable_columns=dataframe2.columns, 
        summable_columns=dataframe1.columns)
    
    # Return value must be of a sequence of pandas.DataFrame
    return df,
