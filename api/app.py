import os
from fastapi import FastAPI
from pydantic import BaseModel
import xgboost as xgb
import pandas as pd
from pathlib import Path

# CONTOURNEMENT MLFLOW : On s'assure que le stockage local est autorisé
os.environ["MLFLOW_ALLOW_FILE_STORE"] = "true"

app = FastAPI(title="Rossmann Sales API")

# ---------------------------------------------------------
# CORRECTION DU CHEMIN : Chemin relatif universel
# ---------------------------------------------------------
# __file__ représente ce fichier (api/app.py)
# .parent.parent remonte à la racine du projet (retail_mlops ou /app)
BASE_DIR = Path(__file__).resolve().parent.parent

# On construit le chemin dynamiquement vers le modèle XGBoost
MODEL_FILE = BASE_DIR / "mlruns" / "1" / "models" / "m-d696f98697b4409eb1b5dd14525e35d2" / "artifacts" / "model.ubj"

# Vérification pour s'assurer que le fichier est bien trouvé
if not MODEL_FILE.exists():
    raise FileNotFoundError(f"Le fichier est introuvable au chemin exact : {MODEL_FILE}")

# Chargement direct via XGBoost
model = xgb.Booster()
model.load_model(str(MODEL_FILE))

class SalesRequest(BaseModel):
    Store: int
    DayOfWeek: int
    Promo: int
    Year: int
    Month: int

@app.post("/predict")
def predict_sales(data: SalesRequest):
    # Transformation de la requête JSON en DataFrame pandas
    input_data = pd.DataFrame([data.model_dump()])
    
    # Conversion au format natif DMatrix pour XGBoost
    dmatrix = xgb.DMatrix(input_data)
    
    # Prédiction
    prediction = model.predict(dmatrix)
    
    return {
        "store_id": data.Store,
        "prediction_euros": round(float(prediction[0]), 2)
    }