from ..extensions import db
from datetime import datetime
from .article_tags import article_tags  # Importation  de la table d'association


class Article(db.Model):
    __tablename__ = 'articles'  # Définition du nom de la table
    id = db.Column(db.Integer, primary_key=True)  # Clé primaire
    title = db.Column(db.String(100), nullable=False)  # Titre de l'article
    description = db.Column(db.Text, nullable=False)  # Contenu de l'article
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Clé étrangère vers l'utilisateur
    created_at = db.Column(db.DateTime, default=datetime.now)  # Date de création
    
    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.user_id = user_id
    
    # Relation plusieurs-à-plusieurs entre les articles et les tags
    tags = db.relationship('Tag', secondary=article_tags,
                           backref=db.backref('articles', lazy='dynamic'))

    def to_dict(self):
        """ Convertit l'objet Article en dictionnaire pour une sérialisation facile / retourne un dictionnaire avec les informations essentielles de l'article """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            #'user_id': self.user_id,
            #'created_at': self.created_at.isoformat()
            'author': self.user.username, # Accès au nom d'utilisateur via la relation backref
            'tags': [tag.name for tag in self.tags]  # Liste des noms de tags associés
        }