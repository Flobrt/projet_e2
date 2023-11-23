# Import de l'applicaiton depuis le dossier /app_flask/
from app_flask import app
import warnings

warnings.filterwarnings("ignore")

# Si appel le script run.py
if __name__ == '__main__':
    app.run(debug=True)
    
# from flask import Flask
# # import ssl
# import warnings

# warnings.filterwarnings("ignore")
# app = Flask(__name__)

# if __name__ == '__main__':
#     # context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
#     # context.load_cert_chain('./certificats/cert.pem', './certificats/key.pem')
#     app.run(debug=True, host='0.0.0.0', port=5000)