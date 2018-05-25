"""
Products API Module to handle PRODUCTS API Calls
"""

import logging

from flask_restplus import Resource

from pvh_digital.api.product.business import get_product
from pvh_digital.api.product.serializers import product_serializer
from pvh_digital.api.product.parsers import product_arguments
from pvh_digital.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('product', description='Product API')


@ns.route('/<string:product_id>')
@api.response(404, 'Product not found')
class Product(Resource):
    """
    Product API
    """
    @api.expect(product_arguments)
    def get(self, product_id, store_id=None):
        """
        Returns a product.
        """
        return api.marshal(get_product(product_id), product_serializer)
