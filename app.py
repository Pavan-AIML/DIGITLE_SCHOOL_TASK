from fastapi import FastAPI, Body, Query
from pydantic import BaseModel
import uvicorn
from typing import Dict
import pickle
import json


"""
Creating an instance of FastAPI application.

"""


app  = FastAPI() # Fast API is used to create a web application instance.

class PredictedRequest(BaseModel):
    year:int 
    month:int



# to load it in the serb=ver not to include in the requests that is why not after the request .


pickle_in = open("regression_model.pkl", "rb") # rb is mode to open pikle file
regression_model = pickle.load(pickle_in) # loading the model from pikle 

"""
creating a GET route with end point (/) when client will send get request
then the function below this will be executed.

"""
@app.get("/")
def index():
    return{"message": "Hello, world, regression model"}



# post request to get the input from user to your emndpoint.

"""
Creating an POST route wit (/predict/) end point. 
When user will send the post request to http://127.0.0.1:8000/predict/
with year and month as a int query in the same format. 

"""

@app.post("/predict/") #defining the json structure
# defining the variable in terms of json.
def predicted_value(year: int =Query(...), month: int=Query(...)): 
    # json_data = json.load(body_param)
    predicted_values = regression_model.predict([[year, month]])
    return {
            "prediction":predicted_values[0].round(0)
            }

# @app.put("/update/")
# def update_model_data(year: int = Query(...), month: int = Query(...)):
#     return {"message": f"Model updated with year={year} and month={month}"}

# # DELETE request to delete some resource or model (again, placeholder example)
# @app.delete("/delete/")
# def delete_model_data(year: int = Query(...), month: int = Query(...)):

#     return {"message": f"Model data for year={year} and month={month} deleted"}
    
# here we have created the local host server locally 

if __name__ == '__main__':

    """
    Starting ASGI server with unicorn to listen all the http requests, 
    run the FastAPI instance by running the app.
    Ip address of the local machine is 127.0.0.1
    
    """

    uvicorn.run(app, host='127.0.0.1', port=8000)

