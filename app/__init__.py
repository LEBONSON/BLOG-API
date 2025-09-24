import os   # Importation du module os pour accéder aux variables d'environnement
from flask import Flask, Blueprint  # Importation de Flask et Blueprint pour la création de l'application et des blueprints
from .extensions import db          # Importation de l'instance de SQLAlchemy pour la gestion de la base de données
#from .api.routes import api_dp      # Importation du blueprint pour les routes de l'API
from config import config           # Importation du dictionnaire de configurations
from .models import init_db         # Importation de la fonction d'initialisation de la base de données

from .api.user_routes import user_dp        # Importation du blueprint pour les routes utilisateur
from .api.article_routes import article_dp  # Importation du blueprint pour les routes article
from .api.tag_routes import tag_dp          # Importation du blueprint pour les routes tag

def create_app(config_name=None):
    # Chargez la configuration
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'default') # Utilisation de  'default' si FLASK_ENV n'est pas défini
    
    app = Flask(__name__) # Création de l'application Flask
    app.config.from_object(config[config_name]) # Chargement de la configuration

    # Initialisation des extensions
    db.init_app(app)

    #Inititialisation de la base de données
    #execute_init_db(app)

    # Enregistrement des blueprints 
    api_dp = Blueprint('api', __name__, url_prefix='/api') # Création d'un Blueprint pour l'API avec le préfixe /api qui sera commun à toutes les routes de l'API
    
    api_dp.register_blueprint(user_dp) # Enregistrement du blueprint utilisateur
    api_dp.register_blueprint(article_dp) # Enregistrement du blueprint article
    api_dp.register_blueprint(tag_dp) # Enregistrement du blueprint tag
    
    app.register_blueprint(api_dp) # Enregistrement du blueprint API dans l'application principale

    return app  # Retourne l'application Flask créée

def execute_init_db(app): # Fonction pour initialiser la base de données
    with app.app_context(): # Assurez-vous que nous sommes dans le contexte de l'application
        init_db() # Initialisation de la base de données