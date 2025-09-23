from ..models.tag import Tag # Importation du modèle Tag
from ..extensions import db # Importation de l'extension db pour interagir avec la base de données
from werkzeug.exceptions import BadRequest # Importation de l'exception BadRequest pour gérer les erreurs de requête 

def create(data:dict) -> Tag:
    """
    Crée un nouveau tag dans la base de données.
    
    Args:
        data (dict): Un dictionnaire contenant les informations du tag.
        
    Returns:
        Tag: L'objet Tag créé.
        
    Raises:
        BadRequest: Si les données sont invalides ou si le tag existe déjà.
    """
    try:
        name = data["name"]
    except KeyError as e: 
        raise BadRequest(f"Champ manquant dans la requête: {e.args[0]}") #  Gestion des erreurs pour les champs manquants
    
    newTag = Tag(name) # Création d'une nouvelle instance de Tag
    db.session.add(newTag) # Ajoute le nouveau tag à la session de la base de données
    db.session.commit() # Sauvegarde les modifications dans la base de données
    return newTag # Retourne l'objet Tag créé

def find_all():
    """
    Récupère tous les tags de la base de données.
    
    Returns:
        list[Tag]: Une liste d'objets Tag.
    """
    return Tag.query.all() # Retourne tous les tags en utilisant une requête SQLAlchemy

def find_by_id(tag_id) -> Tag:
    """
    Récupère un tag par son ID.
    
    Args:
        tag_id (int): L'ID du tag à récupérer.
        
    Returns:
        Tag: L'objet Tag correspondant à l'ID, ou None s'il n'existe pas.
    """
    return Tag.query.get(tag_id) # Recherche du tag par ID avec SQLAlchemy 

def update(tag_id, data: dict) -> Tag:
    """
    Met à jour les informations d'un tag existant.
    
    Args:
        tag_id (int): L'ID du tag à mettre à jour.
        data (dict): Un dictionnaire contenant les nouvelles informations du tag.
        
    Returns:
        Tag: L'objet Tag mis à jour.
        
    Raises:
        BadRequest: Si le tag n'existe pas ou si les données sont invalides.
    """
    tag = find_by_id(tag_id) # Recherche du tag par ID
    if not tag:
        raise ValueError("Tag non trouvé") # Gestion des erreurs si le tag n'existe pas
    
    for key, value in data.items():
        if hasattr(tag, key) and key != "id": # Vérifie si l'attribut existe et n'est pas l'ID
            setattr(tag, key, value) # Mise à jour des attributs du tag avec les nouvelles valeurs
    db.session.commit() # Sauvegarde les modifications dans la base de données
    return tag # Retourne l'objet Tag mis à jour

def delete_by_id(tag_id):
    """
    Supprime un tag par son ID.
    
    Args:
        tag_id (int): L'ID du tag à supprimer.
        
    Raises:
        BadRequest: Si le tag n'existe pas.
    """
    tag = find_by_id(tag_id) # Recherche du tag par ID
    if not tag:
        raise ValueError("Tag non trouvé") # Gestion des erreurs si le tag n'existe pas
    Tag.query.filter_by(id=tag_id).delete() # Supprime le tag de la base de données en utilisant une requête filtrée
    #db.session.delete(tag) # Supprime le tag de la session de la base de données
    db.session.commit() # Sauvegarde les modifications dans la base de données
    return {"message": "Tag supprimé avec succès"} # Retourne un message de succès

