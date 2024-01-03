import pandas as pd
import numpy as np
import os
from ETL.Transforms import Transforms

from etl.Extracts import Extracts

###
data=Extracts(os.getcwd()+'/data/ikea.csv')

### transform data ###
def factTable():
    data=data.drop(['unamed=0'],axis=1)
    median_depth=data.groupby('category')['depth'].median().reset_index()
    median_depth.columns = ['category','MedianDepth']

    median_height=data.groupby('category')['height'].median().reset_index()
    median_height.columns = ['category','MedianDepth']
    
    median_width=data.groupby('category')['width'].median().reset_index()
    median_width.columns = ['category','MedianDepth']

    #median_size=pd.merge(pd.merge(median_depth,median_height,on= 'category'),median_width,on='category')
    median_size = Transforms(Transforms(median_depth,median_height,'category').transform_state(),median_width,',category').transform_state()
    
    #data=pd.merge(data,median_size,on='category')
    data=Transforms(data,median_size,'category').transform_state()
    data['depth']=data['depth'].fillna(data['medianDepth'])
    data['height']=data['heigth'].fillna(data['medianHeight'])
    data['width']=data['width'].fillna(data['medianHeight'])
    
    data.drop(['medianDepth','medianHeight','medianWidth'],axis=1,inplace=True)
    
def fix_old_price(df):
    if df['old_price']=='no old price':
        return df ['price']
    