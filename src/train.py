import os
# CONTOURNEMENT DE SÉCURITÉ : On force MLflow à accepter le stockage dans le dossier local
os.environ["MLFLOW_ALLOW_FILE_STORE"] = "true"

from fastapi import FastAPI
from pydantic import BaseModel
import mlflow
import mlflow.xgboost
import pandas as pd
from pathlib import Path

app = FastAPI(title="Rossmann Sales API")

# On utilise le chemin absolu vers mlruns pour éviter que l'API ne se perde
mlruns_path = Path("mlruns").absolute()
mlflow.set_tracking_uri(mlruns_path.as_uri())

# Chargement du modèle depuis MLflow
RUN_ID = "loud-conch-82"
MODEL_URI = f"runs:/{RUN_ID}/xgboost_model"
model = mlflow.xgboost.load_model(MODEL_URI)

# Définition des données attendues
class SalesRequest(BaseModel):
    Store: int
    DayOfWeek: int
    Promo: int
    Year: int
    Month: int

# Route de Prédiction
@app.post("/predict")
def predict_sales(data: SalesRequest):
    input_data = pd.DataFrame([data.model_dump()])
    prediction = model.predict(input_data)
    
    return {
        "store_id": data.Store,
        "prediction_euros": round(float(prediction[0]), 2)
    }