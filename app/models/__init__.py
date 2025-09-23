from ..extensions import db # Importation de l'instance SQLAlchemy
from .user import User, init_user_table # Importation de l'utilisateur pour enregistrer le modèle avec SQLAlchemy et la fonction d'initialisation de la table User
from .article import Article # Importation de l'article pour enregistrer le modèle avec SQLAlchemy
from .tag import Tag, init_table_tag # Importation du tag pour enregistrer le modèle avec SQLAlchemy
from .article_tags import article_tags # Importation de la table d'association pour enregistrer le modèle avec SQLAlchemy

def init_db():
    db.drop_all()  # Suppréssion de toutes les tables définies dans les modèles
    db.create_all()  # Création de toutes les tables définies dans les modèles
    print(".......... La base de données a été initialisée avec succès ..........")
    
    init_user_table()  # Initialisation de la table User avec des données de test
    init_table_tag()   # Initialisation de la table Tag avec des données de test
