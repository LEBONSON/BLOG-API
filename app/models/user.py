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
    
 # Initialisation de la table User avec des données de test   
def init_user_table():
    # Création d'un nouvel utilisateur
    user1 = User("lebonson", "lenbonson23@gmail.com","lebonson123") 
    user2 = User("johndoe", "johndoe@yahoo.fr", "johndoe123")
    user3 = User("janedoe", "janedoe","janedoe123")

    # Ajout de l'utilisateur à la session
    db.session.add(user1) 
    db.session.add(user2)
    db.session.add(user3)
    
    db.session.commit() # Enregistrement des modifications dans la base de données
    print(".......... La table User a été initialisée avec succès ..........")    