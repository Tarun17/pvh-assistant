"""
Restplus API object for Products & error handlers.
"""

import logging

from flask_restplus import Api

from pvh_digital.api.product.business import ProductNotFound

log = logging.getLogger(__name__)

api = Api(version='1.0', title='PVH Digital API',
          description='PVH Digital Assistant Backend API')


@api.errorhandler(ProductNotFound)
def handle_key_error(error):
    """
    Product Not found Handler
    :param error: error
    :return: Error message json
    """
    log.debug(str(error))
    return {'message': str(error)}, 404
