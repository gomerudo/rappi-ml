import os
from flask import Flask
# from flask import redirect, url_for
from werkzeug.middleware.proxy_fix import ProxyFix
import rappiml.app_config
import rappiml.backend.api


def create_app(test_config=None):

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object(rappiml.app_config)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # # ensure the instance folder exists (??????)
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass


    app.register_blueprint(rappiml.backend.api.bp)

    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

    # # TODO: check if it should be here. Nginx should do the trick as well
    # @app.route('/')
    # def rootindex():
    #     return redirect(url_for('index.index'))

    return app
