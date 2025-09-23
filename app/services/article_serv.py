from ..models.article import Article # Importation du modèle Tag
from ..extensions import db # Importation de l'extension db pour interagir avec la base de données
from werkzeug.exceptions import BadRequest # Importation de
from ..models.tag import Tag # Importation du modèle Tag l'exception BadRequest pour gérer les erreurs de requête
def create(data:dict) -> Article:
    """
    Crée un nouvel article dans la base de données.
    
    Args:
        data (dict): Un dictionnaire contenant les informations de l'article.
        
    Returns:
        Article: L'objet Article créé.
        
    Raises:
        BadRequest: Si les données sont invalides ou si l'article existe déjà.
    """
    try:
        title = data["title"]
        description = data["description"]
        user_id = data["user_id"]
    except KeyError as e: 
        raise BadRequest(f"Champ manquant dans la requête: {e.args[0]}") #  Gestion des erreurs

    new_article = Article(title, description, user_id) # Création d'une nouvelle instance de Tag
    db.session.add(new_article) # Ajoute le nouveau article à la session de la base de données
    db.session.commit() # Sauvegarde les modifications dans la base de données
    return new_article # Retourne l'objet Article créé

def find_all() -> list[Article]:
    """
    Récupère tous les articles de la base de données.
    
    Returns:
        list[Article]: Une liste d'objets Article.
    """
    return Article.query.all() # Retourne tous les articles en utilisant une requête SQLAlchemy

def find_by_id(article_id) -> Article:
    """
    Récupère un article par son ID.
    
    Args:
        article_id (int): L'ID de l'article à récupérer.
        
    Returns:
        Article: L'objet Article correspondant à l'ID, ou None s'il n'existe pas.
    """
    return Article.query.get(article_id) # Recherche du tag par ID avec SQLAlchemy 

def update(article_id, data: dict) -> Article:
    """
    Met à jour les informations d'un article existant.
    
    Args:
        article_id (int): L'ID de l'article à mettre à jour.
        data (dict): Un dictionnaire contenant les nouvelles informations de l'article.
        
    Returns:
        Article: L'objet Article mis à jour.
        
    Raises:
        BadRequest: Si l'article n'existe pas ou si les données sont invalides.
    """
    article = find_by_id(article_id) # Recherche de l'article par ID
    if not article:
        raise ValueError("Article non trouvé") # Gestion des erreurs si l'article n'existe pas
    
    for key, value in data.items():
        if hasattr(article, key) and key != "id": # Vérifie si l'attribut existe et n'est pas l'ID
            setattr(article, key, value) # Mise à jour des attributs de l'article avec les nouvelles valeurs
    db.session.commit() # Sauvegarde les modifications dans la base de données
    return article # Retourne l'objet Article mis à jour

def delete_by_id(article_id):
    """
    Supprime un article par son ID.
    
    Args:
        article_id (int): L'ID de l'article à supprimer.
        
    Raises:
        BadRequest: Si l'article n'existe pas.
    """
    article = find_by_id(article_id) # Recherche de l'article par ID
    if not article:
        raise ValueError("Article non trouvé") # Gestion des erreurs si l'article n'existe pas
    Article.query.filter_by(id=article_id).delete() # Supprime l'article de la base de données en utilisant une requête filtrée
    # Alternativement, on peut utiliser la méthode suivante:
    #db.session.delete(article) # Supprime l'article de la session de la base de données
    db.session.commit() # Sauvegarde les modifications dans la base de données
    return {"message": "Article supprimé avec succès"}

def add_tag_to_article(data: dict):
    """
    Ajoute un tag à un article.
    
    Args:
        data (dict): Un dictionnaire contenant 'article_id' et 'tag_id'.
        
    Returns:
        Article: L'objet Article mis à jour avec le nouveau tag.
        
    Raises:
        BadRequest: Si l'article ou le tag n'existe pas, ou si les données sont invalides.
    """
    try:
        article_id = data["article_id"]
        tag_id = data["tag_id"]
    except KeyError as e:
        raise BadRequest(f"Champ manquant dans la requête: {e.args[0]}") # Gestion des erreurs
    
    article = find_by_id(article_id)
    tag = Tag.query.get(tag_id)

    if not article or not tag:
        raise ValueError("Article ou Tag non trouvé") # Gestion des erreurs si l'article ou le tag n'existe pas 
    
    article.tags.append(tag) # Ajoute le tag à l'article
    db.session.commit() # Sauvegarde les modifications dans la base de données
    return article # Retourne l'objet Article mis à jour

