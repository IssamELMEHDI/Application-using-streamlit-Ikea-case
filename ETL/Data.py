import pandas as pd
import numpy as np
import os

from ETL.Extracts import Extracts
from ETL.Transforms import Transforms

#############################################################################
###                                                                       ###
###                             Extracts data                             ###
###                                                                       ###
#############################################################################

data = Extracts(os.getcwd() +'/data/ikea.csv','csv').load_data()

def fix_old_price(df):
    
    # fill in price to old_price for No old price
    if df['old_price']  == 'No old price':              
        return df['price']

    # remove SR and , from old_price                            
    elif df['old_price'][-4:] != 'pack':                
        return float(str(df['old_price'])[3:].replace(',','')) 
                                                               
    else:
        return np.nan

#############################################################################
###                                                                       ###
###                            Transform Data                             ###
###                                                                       ###
#############################################################################
def factTable(data):
    data=data.drop(['Unnamed: 0'],axis=1)
    median_depth=data.groupby('category')['depth'].median().reset_index()
    median_depth.columns = ['category','medianDepth']

    median_height=data.groupby('category')['height'].median().reset_index()
    median_height.columns = ['category','medianHeight']

    median_width=data.groupby('category')['width'].median().reset_index()
    median_width.columns = ['category','medianWidth']

    #median_size = pd.merge(pd.merge(median_depth,median_height,on='category'),median_width,on='category')
    median_size = Transforms(Transforms(median_depth,median_height,'category').transform_state(),median_width,'category').transform_state()

    #data=pd.merge(data,median_size,on='category')
    data=Transforms(data,median_size,'category').transform_state()
    data['depth']=data['depth'].fillna(data['medianDepth'])
    data['height']=data['height'].fillna(data['medianHeight'])
    data['width']=data['width'].fillna(data['medianHeight'])

    data.drop(['medianDepth','medianHeight','medianWidth'],axis=1 ,inplace=True)
    # create new colum price_diff to help identified is there any different
    # between price and old_price

    data['price_diff']=(data['old_price']!='no old price')

    #apply the function 
    data['old_price']=data.apply(fix_old_price,axis=1)
    data[['price','old_price','price_diff']]
    data['old_price']=data['old_price'].fillna(data['price'])
    
    return data