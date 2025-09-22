import os
from flask import Flask
from .extensions import db
from .api.routes import api_dp
from config import config

def create_app(config_name=None):
    # Chargez la configuration
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'default')
    
    app = Flask(__name__) 
    app.config.from_object(config[config_name])

    # Initialisation des extensions
    db.init_app(app)

    # Enregistrement des blueprints 
    app.register_blueprint(api_dp, url_prefix='/api')

    return app