"""
Serializer for search api
"""

from flask_restplus import fields
from pvh_digital.api.restplus import api


price_serializer = api.model('price_serializer', {
    'currency': fields.String(required=True, description='price'),
    'currency_sign': fields.String(required=True, description='currency_sign'),
    'value': fields.String(required=True, description='value'),
})

search_serializer = api.model('search_serializer', {
    'id': fields.String(readOnly=True, description='id'),
    'style_description': fields.String(required=True, description='style_description', attribute='description'),
    'price': fields.Nested(api.models['price_serializer'], description='price'),
    'image': fields.String(readOnly=True, description="image")
})
