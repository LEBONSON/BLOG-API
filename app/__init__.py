import os
from flask import Flask
from .extensions import db
from .api.routes import api_dp
from config import config
from .models import init_db

def create_app(config_name=None):
    # Chargez la configuration
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'default') # Utilisation de  'default' si FLASK_ENV n'est pas défini
    
    app = Flask(__name__) # Création de l'application Flask
    app.config.from_object(config[config_name]) # Chargement de la configuration

    # Initialisation des extensions
    db.init_app(app)

    #Inititialisation de la base de données
    execute_init_db(app)

    # Enregistrement des blueprints 
    app.register_blueprint(api_dp, url_prefix='/api')

    return app 

def execute_init_db(app):
    with app.app_context():
        init_db() # 