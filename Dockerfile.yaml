# 1. Image de base allégée
FROM python:3.10-slim

# 2. Dossier de travail dans le conteneur
WORKDIR /app

# 3. Copier les dépendances et les installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copier le code de l'API et la base MLflow (qui contient le modèle)
COPY api/ ./api/
COPY mlruns/ ./mlruns/

# 5. Forcer MLflow à lire le dossier local à l'intérieur du conteneur
ENV MLFLOW_ALLOW_FILE_STORE=true

# 6. Exposer le port de l'API
EXPOSE 8000

# 7. Commande de lancement (0.0.0.0 permet d'accepter les connexions externes)
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]