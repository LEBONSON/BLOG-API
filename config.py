import os

class Config:
    """" Classe de configuration de base pour l'application """
    SECRET_KEY = os.environ.get("SECRET_KEY") or ""
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """"Configuration pour l'environnement de développement. """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")


class ProductionConfig(Config):
    """ Configuration pour l'environnement de développement. """
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or ''


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}