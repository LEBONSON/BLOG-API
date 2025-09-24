import os

# Classe de configuration de base et ses dérivées pour différents environnements
class Config:
    """" Classe de configuration de base pour l'application """
    SECRET_KEY = os.environ.get("SECRET_KEY") or "" # Clé secrète pour la sécurité, récupérée depuis les variables d'environnement ou une chaîne vide par défaut
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Désactivation du suivi des modifications pour SQLAlchemy pour économiser les ressources

# Classe de configuration pour l'environnement de développement
class DevelopmentConfig(Config):
    """"Configuration pour l'environnement de développement. """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

# Classe de configuration pour l'environnement de production et de déploiement de l'application
class ProductionConfig(Config):
    """ Configuration pour l'environnement de développement. """
    DEBUG = False # Désactivation du mode debug pour la production
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or '' # Utilisation de la variable d'environnement DATABASE_URL ou une chaîne vide si non définie

# Dictionnaire pour accéder facilement aux configurations
config = {
    'development': DevelopmentConfig, 
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
