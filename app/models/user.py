from ..extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users' # Définition du nom de la table
    id = db.Column(db.Integer, primary_key=True) # Clé primaireale
    username = db.Column(db.String(20), unique=True, nullable=False) # Nom d'utilisateur
    email = db.Column(db.String(80), unique=True, nullable=False) # Email
    password = db.Column(db.String(80), nullable=False) # Hash du mot de passe
    created_at = db.Column(db.DateTime, default=datetime.now) # Date de création

    articles = db.relationship('Article', backref='author', lazy=True) # Relation one to many : un utilisateur peut avoir plusieurs articles et un article appartient à un utilisateur

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    def to_dict(self):
        """" Convertit l'objet User en dictionnaire pour une sérialisation facile / retourne un dictionnaire avec les informations essentielles de l'utilisateur """
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            #'created_at': self.created_at.isoformat()
        }