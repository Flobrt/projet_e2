# Import de l'applicaiton depuis le dossier /app_flask/
from app_flask import app
import warnings

warnings.filterwarnings("ignore")

# Si appel le script run.py
if __name__ == '__main__':
    app.run(debug=True)