import os

from flask import Flask
from flask_cors import CORS

from shortener_url.shortenerApp.routes import shortlinks_blueprint


app = Flask(__name__)
CORS(app)

app_settings = os.getenv(
    'APP_SETTINGS',
    'shortener_url.config.DevelopmentConfig'
)
app.config.from_object(app_settings)
app.register_blueprint(shortlinks_blueprint)

@app.route('/')
def home():
    return {"Home": "Welcome To Shortener App"}
