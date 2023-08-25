# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 01:09:23 2023

@author: Umesh Kumar
"""

from fastapi import FastAPI
from pydantic import BaseModel

import pickle
import json


app = FastAPI()

class model_input(BaseModel):
    
    Age : int
    Gender : int
    Location : int
    Subscription_Length_Months : int
    Monthly_Bill : float
    Total_Usage_GB : int
    
    
# Loading the saved model

customer_churn_model = pickle.load(open('trained_model', 'rb'))


@app.post('/customer_churn_prediction')
def churn_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    age_1 = input_dictionary['Age']
    gender1 = input_dictionary['Gender']
    location_1 = input_dictionary['Location']
    subscription = input_dictionary['Subscription_Length_Months']
    m_bill = input_dictionary['Monthly_Bill']
    total_gb = input_dictionary['Total_Usage_GB']
    
    
    input_list = [age_1, gender1, location_1, subscription, m_bill, total_gb]
    
    prediction = customer_churn_model.predict([input_list])
    
    
    if prediction[0]==[0]:
        return 'The Person is not likely to churn'
    else:
        return 'The Person is likely to churn'