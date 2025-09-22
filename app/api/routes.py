from flask import Blueprint

api_dp = Blueprint('api', __name__)

@api_dp.route('/test', methods=['GET'])
def test():
    return "Bienvenue sur ce nouveau projet Flask !"
