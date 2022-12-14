# from flask import Flask
from .blueprints.example import api_page as api_blueprint
from fastapi import *
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# app = Flask(__name__)
# app.config['DEBUG'] = True
# app.config['CORS_HEADERS'] = 'Content-Type'
# app.register_blueprint(api_blueprint, url_prefix='/example')

# FastAPI
app = FastAPI()

# import templates
templates = Jinja2Templates(directory="./app/templates")

# import static files
app.mount("/static", StaticFiles(directory="./app/static"), name="static")

# blueprint
app.include_router(api_blueprint, prefix="/api")

