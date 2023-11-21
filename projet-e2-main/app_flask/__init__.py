from flask import Flask
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)

UPLOAD_FOLDER = "./app_flask/upload/"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

from .views import app
from .views import *