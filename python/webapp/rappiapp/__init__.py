from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
import rappiapp.app_config
import rappiapp.backend.api
from logging.config import dictConfig


def create_app(test_config=None):

    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    })

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object(rappiapp.app_config)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    app.register_blueprint(rappiapp.backend.api.bp)

    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

    # # TODO: check if it should be here. Nginx should do the trick as well
    # @app.route('/')
    # def rootindex():
    #     return redirect(url_for('index.index'))

    return app
