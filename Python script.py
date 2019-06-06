# The script MUST contain a function named azureml_main
# which is the entry point for this module.
#
###
# This script assign churn status to each subscriber in the data
# To assign the churn status it uses the churn period start date passed as input as dataframe2( either from the uploaded dataset or the web service)

###
import pandas as pd
import numpy as np
import datetime as dt
from RetailChurnTemplateUtility import *

# The entry point function can contain up to two input arguments:
#   Param<dataframe1>: JoinedActivityUserInfor DataFrame
#   Param<dataframe2>: Churn Start Period Date Dataframe
def azureml_main(dataframe1 = None, dataframe2 = None):
    key_column='UserId'
    activity_column='TransactionId'
    
    ChurnPeriod=int(dataframe2.iloc[0]['ChurnPeriod'])
    ChurnThreshold=int(dataframe2.iloc[0]['ChurnThreshold'])
  
    dataframe1['Timestamp']= dataframe1.apply(lambda x : dt.datetime.fromtimestamp(x['Timestamp']).strftime('%Y-%m-%d'), axis=1)
    dataframe1['Parsed_Date']=pd.to_datetime(dataframe1['Timestamp'])
#       Assigning Churn Status
    churnUtil=RetailChurnTemplateUtility(ChurnPeriod,ChurnThreshold)
    outdataframe=churnUtil.assign_churn_status(dataframe1,key_column=key_column,activity_column=activity_column) 
    print 'outdataframe.head()', outdataframe.head()
    print 'outdataframe.dtypes\n', outdataframe.dtypes
    
    
    outdataframe.fillna('Unknown', inplace=True)
    outdataframe['ChurnPeriod']=ChurnPeriod
    to_keep_list=[each for each in outdataframe.columns if each!='Parsed_Date']
    
    #       Return value must be of a sequence of pandas.DataFrame
    return outdataframe[to_keep_list],
