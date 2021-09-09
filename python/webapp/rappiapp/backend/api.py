"""API endpoint to expose the model(s)."""

import requests
from flask import Blueprint
from flask import jsonify
from flask import request
from flask import current_app
from rappiapp.utils import get_db_connection

bp = Blueprint('api', __name__, url_prefix='/analytics/api')


@bp.route('/taken/', methods=['POST'])
def predict_taken():
    """Define endpoint and behaviour to run 'taken' inferences on orders."""
    # Get the JSON data from the original request
    query = request.get_json()

    # Query MLFlow
    r = requests.post(
        'http://ml-server:5000/invocations',
        json=query
    )
    response = r.json()
    current_app.logger.info("MLFlow response" % response)

    # Store info in the DB
    cnx = get_db_connection()
    cursor = cnx.cursor()

    add_inferences = (
        "INSERT IGNORE INTO TakenInferences "
        "(OrderID, ServiceVersion, Result) "
        "VALUES (%s, %s, %s)"
    )

    data_inferences = []
    for obs, res in zip(query['data'], response):
        data_inferences.append((obs[0], 'v1.0', res))

    cursor.executemany(add_inferences, data_inferences)
    cnx.commit()

    cursor.close()
    cnx.close()

    # Return response
    return jsonify(response)
