import io
import json
from flask import Blueprint
from flask import redirect
from flask import jsonify
from flask import request

# import rappiml.app_config


bp = Blueprint('api', __name__, url_prefix='/analytics/api')

@bp.route('/<int:order_id>/taken/', methods=['GET'])
def get_reference_clips(order_id):
    # bin_id = request.args.get('bin', default=0)

    return jsonify(
        status="ok"
    )


# class InvalidUsage(Exception):

#     def __init__(self, message, status_code=None, payload=None):
#         Exception.__init__(self)
#         self.message = message
#         if status_code is not None:
#             self.status_code = status_code
#         self.payload = payload

#     def to_dict(self):
#         rv = dict(self.payload or ())
#         rv['error'] = self.message
#         return rv


# @bp.errorhandler(InvalidUsage)
# def handle_invalid_usage(error):
#     response = jsonify(error.to_dict())
#     response.status_code = error.status_code
#     return response
