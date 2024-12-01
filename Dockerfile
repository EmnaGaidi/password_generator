# Utiliser une image vulnérable connue
FROM vulnerables/web-dvwa

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY . /app

# Installer Python (simule un environnement nécessaire pour l'application)
RUN apt-get update && apt-get install -y python3 python3-pip

# Installer pytest pour les tests
RUN pip3 install pytest

# Point d'entrée par défaut
CMD ["python3", "password_generator.py"]

