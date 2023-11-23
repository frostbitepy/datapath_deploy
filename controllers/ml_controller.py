import pickle
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
import pandas as pd
import numpy as np
#from utils.helper import pre_processing, apply_prediction

router = APIRouter()

# Load the trained model using pickle
with open('modelo_entrenado.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

class PulsarPredictionRequest(BaseModel):
    Mean_Integrated: float
    SD: float
    EK: float
    Skewness: float
    Mean_DMSNR_Curve: float
    SD_DMSNR_Curve: float
    EK_DMSNR_Curve: float
    Skewness_DMSNR_Curve: float

@router.post("/predict/")
def predict_pulsar(data: PulsarPredictionRequest):
    try:
        # Convert the input data to a format suitable for prediction
        input_data = pd.DataFrame([{
            'Mean_Integrated': data.Mean_Integrated,
            'SD': data.SD,
            'EK': data.EK,
            'Skewness': data.Skewness,
            'Mean_DMSNR_Curve': data.Mean_DMSNR_Curve,
            'SD_DMSNR_Curve': data.SD_DMSNR_Curve,
            'EK_DMSNR_Curve': data.EK_DMSNR_Curve,
            'Skewness_DMSNR_Curve': data.Skewness_DMSNR_Curve,
        }])

        # Make predictions using the loaded model
        predictions = loaded_model.predict(input_data)

        return {"prediction": int(predictions[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))