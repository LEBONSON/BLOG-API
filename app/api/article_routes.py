from flask import Blueprint, request, jsonify # Importation de Flask et de ses modules
from werkzeug.exceptions import BadRequest # Importation des exceptions de Werkzeug
from ..services import article_serv # Importation du service article

article_dp = Blueprint('article_api', __name__, url_prefix='/articles') # Création d'un Blueprint pour les routes article   

@article_dp.route('', methods=['GET']) # Définition de la route pour récupérer tous les articles
def get_article():
    articles = article_serv.find_all() # Appel du service pour récupérer tous les articles
    article_dic = [article.to_dict() for article in articles] # Conversion des articles en dictionnaires
    return {"articles": article_dic}, 200 # Retourne la liste des articles dans un dictionnaire avec un code de statut

@article_dp.route('', methods=['POST']) # Définition de la route pour créer un article
def create_article():
    data = request.get_json() # Récupération des données JSON de la requête
    if not data:
        raise BadRequest("Données JSON manquantes. Le corps de la requête doit être au format JSON.") # Levée d'une exception si les données sont manquantes
    new_article = article_serv.create_article(data) # Appel du service pour créer un article
    return jsonify(new_article), 201 # Retourne l'article créé avec un code de statut

@article_dp.route('/<int:article_id>', methods=['PUT']) # Définition de la route pour mettre à jour un article
def update_article(article_id):
    data = request.get_json() # Récupération des données JSON de la requête
    if not data:
        raise BadRequest("Données JSON manquantes. Le corps de la requête doit être au format JSON.") # Levée d'une exception si les données sont manquantes
    try:
        updated_article = article_serv.update_article(article_id, data) # Appel du service pour mettre à jour un article
        return jsonify(updated_article), 200 # Retourne l'article mis à jour avec un code de statut
    except ValueError as e:
        return jsonify({"error": str(e)}), 404 # Retourne une erreur si l'article n'est pas trouvé
    

@article_dp.route('/<int:article_id>', methods=['DELETE']) # Définition de la route pour supprimer un article
def delete_article(article_id):
    message = article_serv.delete_article(article_id) # Appel du service pour supprimer un article
    return jsonify({"message": message}), 200 # Retourne un message de succès avec un code de statut


@article_dp.route('/add_tag_to_article', methods=['POST']) # Définition de la route pour ajouter un tag à un article
def add_tag_to_article():
    data = request.get_json() # Récupération des données JSON de la requête
    if not data:
        raise BadRequest("Données JSON manquantes. Le corps de la requête doit être au format JSON.") # Levée d'une exception si les données sont manquantes
    article = article_serv.add_tag_to_article(data) # Appel du service pour ajouter un tag à un article
    return jsonify(article.to_dict()), 200 # Retourne l'article mis à jour avec un code de statut et une conversion en dictionnaire qui contient les tags
 