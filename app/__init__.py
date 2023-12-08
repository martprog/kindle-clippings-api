from flask import Flask
from app.views import data_bp

app = Flask(__name__)

app.register_blueprint(data_bp, url_prefix="/api")