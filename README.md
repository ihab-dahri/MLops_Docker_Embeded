# Retail MLOps - Prédiction de Chiffre d'Affaires 🛒📈

Cette application est une API Machine Learning développée avec **FastAPI** et hébergée via **Docker**. Elle embarque un modèle **XGBoost** pré-entraîné capable de prédire le chiffre d'affaires journalier (en euros) d'une boutique retail en fonction de différents paramètres d'entrée.

Ce dépôt intègre **Git LFS** pour la gestion des fichiers volumineux (modèles `.xgb` et `.pkl`).

## Architecture Technique

*   **API Framework :** FastAPI (Python)
*   **Modèle ML :** XGBoost (Regression)
*   **Conteneurisation :** Docker
*   **Gestion de version des modèles :** Git LFS
*   **Serveur Web :** Uvicorn

##  Prérequis

Avant de commencer, assurez-vous d'avoir installé sur votre machine :
- [Python 3.9+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/products/docker-desktop/)
- [Git LFS](https://git-lfs.com/) (Indispensable pour récupérer les fichiers du modèle)

##  Installation & Déploiement

### 1. Cloner le dépôt et récupérer le modèle
Puisque le modèle est stocké via Git LFS, l'initialisation nécessite de bien tirer les gros fichiers.

```bash
# Cloner le dépôt
git clone [https://github.com/ihab-dahri/MLops_Docker_Embeded.git](https://github.com/ihab-dahri/MLops_Docker_Embeded.git)

# Entrer dans le répertoire
cd MLops_Docker_Embeded

# S'assurer que les fichiers LFS sont bien téléchargés
git lfs pull
