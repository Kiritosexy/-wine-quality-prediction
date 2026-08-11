from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "random_forest.pkl"
PREPROCESSOR_PATH = BASE_DIR / "models" / "preprocessor.pkl"

app = FastAPI (
    tittle= "Wine Qualite Prediction Api",
    description = "API de prediction de la qualité du vin",
    version = "1.0.0"
)

model = joblib.load(MODEL_PATH)
preprocessor = joblib.load(PREPROCESSOR_PATH)

class WineData(BaseModel) :
    fixed_acidity : float
    volatile_acidity : float
    citric_acid : float
    residual_sugar : float
    chlorides : float
    free_sulfur_dioxide  : float
    total_sulfur_dioxide : float
    density : float
    ph : float
    sulphates : float
    alcohol : float
    type : str

@app.get("/")
def home():
    return{
        "message" : "Wine quality prediction API",
        "status" : "API is running"
    }
    
@app.post("/predict")
def predict_wine(data : WineData):
    input_data = pd.DataFrame([{
        "fixed_acidity": data.fixed_acidity,
        "volatile_acidity": data.volatile_acidity,
        "citric_acid": data.citric_acid,
        "residual_sugar": data.residual_sugar,
        "chlorides": data.chlorides,
        "free_sulfur_dioxide": data.free_sulfur_dioxide,
        "total_sulfur_dioxide": data.total_sulfur_dioxide,
        "density": data.density,
        "ph": data.ph,
        "sulphates": data.sulphates,
        "alcohol": data.alcohol,
        "type": data.type
    }])
    
    input_processed = preprocessor.transform(input_data)
    prediction = model.predict(input_processed)[0]
    
    return {
        "prediction": prediction
    }