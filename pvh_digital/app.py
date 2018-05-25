"""
Module for PVH Digital Assistant
Creating and Setting up Flask object and
Starting Execution of Application
"""
import logging.config
import pvh_digital.settings as settings
from pvh_digital.api.product.endpoints.products import ns as products_namespace
from pvh_digital.api.search.endpoints.search import ns as search_namespace
from pvh_digital.api.restplus import api
from flask import Flask, Blueprint


log = logging.getLogger(__name__)


def configure_app(flask_app):
    """
    Setting up config for flask application object as per settings files
    :param flask_app: Flask Application Object
    :return: None
    """
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
    flask_app.config['SERVER_NAME'] = 'localhost:5000'



def initialize_app(flask_app):
    """
    Initalizes blueprints
    :param flask_app: Application Flask App
    :return: Flask object
    """
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(products_namespace)
    api.add_namespace(search_namespace)
    flask_app.register_blueprint(blueprint)
    return flask_app


def main():
    """
    Main Function Starting Execution of Application
    :return: Flask Object
    """
    flask_app = Flask(__name__)
    flask_app = initialize_app(flask_app)
    log.info('Starting development server at http://{}/api/'
             .format(flask_app.config['SERVER_NAME']))
    flask_app.config.update(DEBUG=True)
    return flask_app


app = main()


@app.route('/')
def index():
    """home page"""
    return "PVH Digital Assistant App", 200


if __name__ == "__main__":
    main()

