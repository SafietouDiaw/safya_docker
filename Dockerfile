# 1. Utiliser une image Python officielle comme base
FROM python:3.11-slim

# 2. Définir le dossier de travail dans le conteneur
WORKDIR /app

# 3. Copier le fichier des dépendances
COPY requirements.txt .

# 4. Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copier tout le reste du code dans le conteneur
COPY . .

# 6. Exposer le port que Flask utilise (souvent 5000)
EXPOSE 5000

# 7. Lancer l'application
CMD ["python", "server.py"]