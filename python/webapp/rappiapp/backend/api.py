import requests
from flask import Blueprint
from flask import jsonify
from flask import request
from flask import current_app

bp = Blueprint('api', __name__, url_prefix='/analytics/api')


@bp.route('/taken/', methods=['GET', 'POST'])
def predict_taken():

    r = requests.post(
        'http://ml-server:5000/invocations',
        json=request.get_json()
    )

    response = r.json()
    current_app.logger.info("MLFlow response" % response)
    return jsonify(response)
