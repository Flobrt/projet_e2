from flask import Flask
import warnings
import os

warnings.filterwarnings("ignore")

app = Flask(__name__)

UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', './app_flask/upload/')
# UPLOAD_FOLDER = "./app_flask/upload/"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

from .views import app
from .views import *