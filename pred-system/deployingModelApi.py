!pip install fastapi
!pip install uvicorn
!pip install pickle5
!pip install pydantic
!pip install scikit-learn
!pip install requests
!pip install pypi-json
!pip install pyngrok
!pip install nest-asyncio

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import nest_asyncio
import uvicorn
from pyngrok import ngrok
import numpy as np
import joblib

app = FastAPI()

origins = ["http://localhost:4200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Type"],  # Add this line
)

class ModelInput(BaseModel):
    protocol_type: float
    service: float
    flag: float
    src_bytes: float
    dst_bytes: float
    count: float
    same_srv_rate: float
    diff_srv_rate: float
    dst_host_srv_count: float
    dst_host_same_srv_rate: float

# loading the saved model
clf  = pickle.load(open('INTRUSION_model1.sav', 'rb'))
# Load the scaler
scaler_filename = 'scaler_model1.sav'
scaler = joblib.load(scaler_filename)
@app.post('/INTRUSION_detection')
def intru_predd(input_parameters: ModelInput):
    input_list = [input_parameters.protocol_type,
                  input_parameters.service,
                  input_parameters.flag,
                  input_parameters.src_bytes,
                  input_parameters.dst_bytes,
                  input_parameters.count,
                  input_parameters.same_srv_rate,
                  input_parameters.diff_srv_rate,
                  input_parameters.dst_host_srv_count,
                  input_parameters.dst_host_same_srv_rate]

    input_array = np.array(input_list).reshape(1, -1)
    input_array_scaled = scaler.transform(input_array)
    prediction = clf.predict(input_array_scaled)


    if prediction[0] == 0:
        return {'result': 'ANOMALY'}
    else:
        return {'result': 'NORMAL'}

!ngrok authtoken "******************************"
ngrok_tunnel = ngrok.connect(9000)
print('Public URL:', ngrok_tunnel.public_url)

nest_asyncio.apply()
uvicorn.run(app, port=9000)