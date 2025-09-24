from flask import Blueprint, request, jsonify # Importation de Flask et de ses modules
from werkzeug.exceptions import BadRequest # Importation des exceptions de Werkzeug
from ..services import tag_serv # Importation du service tag

tag_dp = Blueprint('tag_api', __name__, url_prefix='/tags') # Création d'un Blueprint pour les routes tag   

@tag_dp.route('', methods=['GET']) # Définition de la route pour récupérer tous les tags
def get_tag():
    tags = tag_serv.find_all() # Appel du service pour récupérer tous les tags
    tag_dic = [tag.to_dict() for tag in tags] # Conversion des tags en dictionnaires
    return {"tags": tag_dic} # Retourne la liste des tags dans un dictionnaire

@tag_dp.route('', methods=['POST']) # Définition de la route pour créer un tag
def create_tag():
    data = request.get_json() # Récupération des données JSON de la requête
    if not data:
        raise BadRequest("Données JSON manquantes. Le corps de la requête doit être au format JSON.") # Levée d'une exception si les données sont manquantes
    new_tag = tag_serv.create_tag(data) # Appel du service pour créer un tag
    return jsonify(new_tag), 201 # Retourne le tag créé avec un code de statut


@tag_dp.route('/<int:tag_id>', methods=['PUT']) # Définition de la route pour mettre à jour un tag
def update_tag(tag_id):
    data = request.get_json() # Récupération des données JSON de la requête
    if not data:
        raise BadRequest("Données JSON manquantes. Le corps de la requête doit être au format JSON.") # Levée d'une exception si les données sont manquantes
    try:
        updated_tag = tag_serv.update_tag(tag_id, data) # Appel du service pour mettre à jour un tag
        return jsonify(updated_tag), 200 # Retourne le tag mis à jour avec un code de statut
    except ValueError as e:
        return jsonify({"error": str(e)}), 404 # Retourne une erreur si le tag n'est pas trouvé


@tag_dp.route('/<int:tag_id>', methods=['DELETE']) # Définition de la route pour supprimer un tag
def delete_tag(tag_id):
    message = tag_serv.delete_tag(tag_id) # Appel du service pour supprimer un tag
    return jsonify({"message": message}), 200 # Retourne un message de succès avec un code de statut

