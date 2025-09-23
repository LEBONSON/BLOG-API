from ..extensions import db
from datetime import datetime
from .article_tags import article_tags  # Importation  de la table d'association

class Tag(db.Model):
    __tablename__ = 'tags'  # Définition du nom de la table

    id = db.Column(db.Integer, primary_key=True)  # Clé primaire
    name = db.Column(db.String(50), unique=True, nullable=False)  # Nom du tag
    created_at = db.Column(db.DateTime, default=datetime.now)  # Date de création

    def __init__(self, name):
        self.name = name



    def to_dict(self):
        """ Convertit l'objet Tag en dictionnaire pour une sérialisation facile / retourne un dictionnaire avec les informations essentielles du tag """
        return {
            'id': self.id,
            'name': self.name,
            #'created_at': self.created_at.isoformat()
            'articles': [article for article in self.articles]  # Liste des titres des articles associés
        }

# Initialisation de la table Tag avec des données de test
def init_table_tag():
    # Création de nouveaux tags
    tag1 = Tag("Science")
    tag2 = Tag("Technologie")
    tag3 = Tag("Programmation")
    tag4 = Tag("Réseaux")
    tag5 = Tag("Cybersécurité")

    # Ajout des tags à la session
    db.session.add(tag1)
    db.session.add(tag2)
    db.session.add(tag3)
    db.session.add(tag4)
    db.session.add(tag5)

    db.session.commit()  # Enregistrement des modifications dans la base de données
    print(".......... La table Tag a été initialisée avec succès ..........")