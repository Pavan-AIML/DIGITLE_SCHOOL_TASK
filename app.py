from fastapi import FastAPI, Body, Query
from pydantic import BaseModel
import uvicorn
from typing import Dict
import pickle
import json



app  = FastAPI()

"""

 Here we have created this class so that we can have the input as a jason format lile -> 
 { 
 "year":2020,
 "month":10
 }
 
"""

class PredictedRequest(BaseModel):
    year:int 
    month:int

# to load it in the serb=ver not to include in the requests that is why not after the request .


pickle_in = open("regression_model.pkl", "rb") # rb is mode to open pikle file
regression_model = pickle.load(pickle_in) # loading the model from pikle 


@app.get("/")
def index():
    return{"message": "Hello, Stranger"}

# post request to get the input from user to your emndpoint.


@app.post("/predict/") #defining the json structure
# defining the variable in terms of json.
def predicted_value(request:PredictedRequest): 
    # json_data = json.load(body_param)
    predicted_values = regression_model.predict([[request.year, request.month]])
    return {
            "prediction":predicted_values[0].round(0)
            }



    

# here we have created the local host server locally 

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
