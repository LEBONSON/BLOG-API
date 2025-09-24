from flask import Blueprint, request, jsonify # Importation de Flask et de ses modules
from werkzeug.exceptions import BadRequest # Importation des exceptions de Werkzeug qui est utilisé par Flask
from ..services import user_serv # Importation du service utilisateur

user_dp = Blueprint('user_api', __name__, url_prefix='/users') # Création d'un Blueprint pour les routes utilisateur

@user_dp.route('', methods=['POST']) # Définition de la route pour mettre à jour un utilisateur
def create_user():
    data = request.get_json() # Récupération des données JSON de la requête
    if not data:
        raise BadRequest("Données JSON manquantes. Le corps de la requête doit être au format JSON.") # Levée d'une exception si les données sont manquantes
    new_user = user_serv.create_user(data) # Appel du service pour créer un utilisateur
    return jsonify(new_user), 201 # Retourne l'utilisateur créé avec un code de statut


@user_dp.route('', methods=['GET']) # Définition de la route pour récupérer un utilisateur par ID
def get_user():
    users = user_serv.find_all() # Appel du service pour récupérer tous les utilisateurs
    user_dic = [user.to_dict() for user in users] # Conversion des utilisateurs en dictionnaires
    #return jsonify(user_dic), 200 # Retourne la liste des utilisateurs avec un code de statut
    return {"users": user_dic} # Retourne la liste des utilisateurs dans un dictionnaire  

@user_dp.route('/<int:user_id>', methods=['GET']) # Définition de la route pour récupérer un utilisateur par ID
def find_user_by_id(user_id):
    user = user_serv.find_user_by_id(user_id) # Appel du service pour récupérer un utilisateur par ID
    return jsonify(user), 200 # Retourne l'utilisateur avec un code de statut

@user_dp.route('/<int:user_id>', methods=['PUT']) # Définition de la route pour mettre à jour un utilisateur
def update_user(user_id):
    data = request.get_json() # Récupération des données JSON de la requête
    if not data:
        raise BadRequest("Données JSON manquantes. Le corps de la requête doit être au format JSON.") # Levée d'une exception si les données sont manquantes
    try:
        updated_user = user_serv.update_user(user_id, data) # Appel du service pour mettre à jour un utilisateur
        return jsonify(updated_user), 200 # Retourne l'utilisateur mis à jour avec un code de statut
    except ValueError as e:
        return jsonify({"error": str(e)}), 404 # Retourne une erreur si l'utilisateur n'est pas trouvé
    
@user_dp.route('/<int:user_id>', methods=['DELETE']) # Définition de la route pour supprimer un utilisateur
def delete_user(user_id):
    message = user_serv.delete_user(user_id) # Appel du service pour supprimer un utilisateur
    return jsonify({"message": message}), 200 # Retourne un message de succès avec un
