import json
import pickle
import os
import numpy as np
import warnings


__city =None
__data_cols=None
__model=None


current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'artifacts', 'columns.json')
model_path = os.path.join(current_dir,'artifacts', 'Realestate_price_prediction_model.pickle')


def get_city():
    return __city

def load_saved_artifacts():
    print('loading saved artifacts....')
    global __city
    global __data_cols

    with open(file_path,'r')as f:
        __data_cols=json.load(f)['data_columns']
        __city=__data_cols[4:]

    with open(model_path,'rb') as f:
        global __model
        __model=pickle.load(f)  
        print('loading complete....')  

def get_prediction(city,land_size,house_size, lat,lon):
    try:
        loc_index=__data_cols.index(city.lower())
    except:
        loc_index=-1 

    x=np.zeros(len(__data_cols))
    x[0]=land_size
    x[1]=house_size
    x[2]=lat
    x[3]=lon
    if loc_index >=0:
        x[loc_index]=1      

    return round(__model.predict([x])[0],2)

warnings.filterwarnings("ignore", category=UserWarning, message="X does not have valid feature names*")

load_saved_artifacts()
 
if __name__=='__main__':
    print(get_city())
    print(get_prediction('kandy','20','1600','80.65','9.6'))
    print(get_prediction('colombo','20','1600','79.834','8.6'))




    