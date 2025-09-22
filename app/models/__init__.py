from ..extensions import db # Importation de l'instance SQLAlchemy
from .user import User # Importation de l'utilisateur pour enregistrer le modèle avec SQLAlchemy
from .article import Article # Importation de l'article pour enregistrer le modèle avec SQLAlchemy
from .tag import Tag # Importation du tag pour enregistrer le modèle avec SQLAlchemy
from .article_tags import article_tags # Importation de la table d'association pour enregistrer le modèle avec SQLAlchemy

def init_db():
    db.create_all()  # Création de toutes les tables définies dans les modèles
    db.create_all()  # Création de toutes les tables définies dans les modèles
    print(".......... La base de données a été initialisée avec succès ..........")
    