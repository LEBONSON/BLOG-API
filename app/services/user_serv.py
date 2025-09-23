from ..models.user import User # Importation du modèle User
from ..extensions import db # Importation de l'extension db pour interagir avec la base de données
from werkzeug.exceptions import BadRequest # Importation de l'exception BadRequest pour gérer les erreurs de requête

def create_user(data):
    """
    Crée un nouvel utilisateur dans la base de données.
    
    Args:
        data (dict): Un dictionnaire contenant les informations de l'utilisateur.
        
    Returns:
        User: L'objet User créé.
        
    Raises:
        BadRequest: Si les données sont invalides ou si l'utilisateur existe déjà.
    """
    try:
        username = data["username"]
        email = data["email"]
        password = data["password"]
    except KeyError as e: 
        raise BadRequest(f"Champ marquant dans la requête: {e.args[0]}") #  Gestion des erreurs pour les champs manquants
    
    newUser = User(username, email, password) # Création d'une nouvelle instance de User
    db.session.add(newUser) # Ajoute le nouvel utilisateur à la session de la base de données
    db.session.commit() # Sauvegarde les modifications dans la base de données
    return newUser # Retourne l'objet User créé

def find_all() -> list[User]:
    """
    Récupère tous les utilisateurs de la base de données.
    
    Returns:
        list[User]: Une liste d'objets User.
    """
    return User.query.all() # Retourne tous les utilisateurs en utilisant une requête SQLAlchemy
 
def update(user_id, data: dict) -> User:
    """
    Met à jour les informations d'un utilisateur existant.
    
    Args:
        user_id (int): L'ID de l'utilisateur à mettre à jour.
        data (dict): Un dictionnaire contenant les nouvelles informations de l'utilisateur.
        
    Returns:
        User: L'objet User mis à jour.
        
    Raises:
        BadRequest: Si l'utilisateur n'existe pas ou si les données sont invalides.
    """
    user = find_by_id(user_id) # Recherche de l'utilisateur par ID
    if not user:
        raise ValueError("Utilisateur non trouvé") # Gestion des erreurs si l'utilisateur n'existe pas
    
    for key, value in data.items():
        if hasattr(user, key) and key != "id": # Vérifie si l'attribut existe et n'est pas l'ID
            setattr(user, key, value) # Mise à jour des attributs de l'utilisateur avec les nouvelles valeurs
    db.session.commit() # Sauvegarde les modifications dans la base de données
    return user # Retourne l'objet User mis à jour

def find_by_id(user_id) -> User:
    """
    Récupère un utilisateur par son ID.
    
    Args:
        user_id (int): L'ID de l'utilisateur à récupérer.
        
    Returns:
        User: L'objet User correspondant à l'ID, ou None si non trouvé.
    """
    return User.query.get(user_id) # Recherche de l'utilisateur par ID avec SQLAlchemy

def delete_by_id(user_id):
    User.query.filter_by(id=user_id).delete() # Suppression de l'utilisateur par ID
    db.session.commit() # Sauvegarde les modifications dans la base de données
    return {"message": "Utilisateur supprimé avec succès"} # Retourne un message de succès
   
    # Note: Nous pouvons ajouter une gestion des erreurs si nécessaire
    # Par exemple, vérifier si l'utilisateur existe avant de tenter de le supprimer
