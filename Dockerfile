# Utiliser une image Python légère comme base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers du projet
COPY . /app

# Installer les dépendances (pytest pour les tests si nécessaire)
RUN pip install pytest

# Commande par défaut
CMD ["python", "password_generator.py"]
