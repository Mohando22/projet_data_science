# Utiliser une image de base Python
FROM python:3.8-slim

# Définir le répertoire de travail à la racine du conteneur
WORKDIR /

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier les fichiers et dossiers nécessaires dans le conteneur
COPY geo_classif.py .
COPY classif.html .
COPY file_csv/ file_csv/

# Exposer le port 8000
EXPOSE 8000

# Utiliser le serveur HTTP intégré de Python pour servir le fichier HTML
CMD ["python", "-m", "http.server", "8000", "--bind", "0.0.0.0"]
