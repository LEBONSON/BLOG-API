from flask import Blueprint # Importation de Blueprint depuis Flask pour créer des groupes de routes

api_dp = Blueprint('api', __name__) # Création d'un blueprint pour les routes de l'API

@api_dp.route('/test', methods=['GET']) # Route de test pour vérifier que l'API fonctionne et est accessible

# Fonction de test simple qui retourne un message de bienvenue
def test():
    return "Bienvenue sur ce nouveau projet Flask !"
