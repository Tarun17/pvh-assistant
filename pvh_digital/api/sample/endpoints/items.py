"""
Items API Module to handle items API Calls
"""

import logging

from flask import request
from flask_restplus import Resource

from pvh_digital.api.sample.business import create_item, update_item, delete_item
from pvh_digital.api.sample.serializers import item, page_of_items
from pvh_digital.api.sample.parsers import pagination_arguments
from pvh_digital.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('sample/items', description='Sample API')


@ns.route('/<int:id>')
@api.response(404, 'item not found.')
class SampleItem(Resource):
    """
    Sample Item API
    """

    @api.marshal_with(item)
    def get(self, id):
        """
        Returns a sample item.
        """
        return {'id': id}

    @api.expect(item)
    @api.response(204, 'item successfully updated.')
    def put(self, id):
        """
        Updates a sample item.
        """
        return None, 204

    @api.response(204, 'item successfully deleted.')
    def delete(self, id):
        """
        Deletes sample item.
        """

        return None, 204
