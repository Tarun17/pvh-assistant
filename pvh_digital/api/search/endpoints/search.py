"""
Search Endpoints
"""
import logging

from flask import request
from flask_restplus import Resource
from pvh_digital.api.es.connections import conn
from pvh_digital.api.search.parsers import arguments
from pvh_digital.api.search.serializers import search_serializer

from pvh_digital.api.es.filters import search_product
from pvh_digital.api.restplus import api


log = logging.getLogger(__name__)

ns = api.namespace('search', description='Search API')

@ns.route('/items')
class SearchItem(Resource):
    """
    Search API - To HANDlE HTTP search Request for items
    """
    @api.expect(arguments)
    @ns.marshal_with(search_serializer)
    def get(self):
        """
        Returns search results.
        :rtype: json response
        :return: search result
        """
        args = arguments.parse_args(request)
        query = args.get('q')
        resp = search_product(conn, query)


        return resp
