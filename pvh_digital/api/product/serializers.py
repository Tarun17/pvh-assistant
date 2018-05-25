"""
Serializer for Product API
"""

from flask_restplus import fields
from pvh_digital.api.restplus import api

product_detail_image_fields = {}
product_detail_image_fields['actual'] = fields.String()
product_detail_image_fields['thumb'] = fields.String()

price_fields = {}
price_fields['currency'] = fields.String()
price_fields['currency_sign'] = fields.String(),
price_fields['value'] = fields.Float()

class DynamicObject(fields.Raw):
    """
    This class is used for serializing dictionaries
    whose keys are not known beforehand.
    """
    def format(self, value):
        return value

product_serializer = api.model('Product', {
    'id': fields.String(readOnly=True, description='The unique identifier of the product'),
    'style_description': fields.String(description='Product description', attribute='description'),
    'details': fields.String(description='Product details'),
    'color_code': fields.String(description='Product color'),
    'size_code': fields.String(description='Product size'),
    'locale': fields.String(description='Locale of the response'),
    'size_guide': fields.String(description='Size guide'),
    'store_id': fields.String(description='Store of the associate'),
    'division_code': fields.String(),
    'division_name': fields.String(),
    'department_code': fields.String(),
    'department_name': fields.String(),
    'class_code': fields.String(),
    'class_name': fields.String(),
    'style_code': fields.String(),
    'images': fields.List(fields.Nested(product_detail_image_fields)),
    'price': {
        'currency': fields.String(attribute='price.currency'),
        'currency_sign': fields.String(attribute='price.currency_sign'),
        'value': fields.String(attribute='price.value')
    },
    'colors_available': DynamicObject(attribute='colors_available'),
    'sizes_available': DynamicObject(attribute='sizes_available'),
    'variants': DynamicObject(attribute='variants'),
    'availability': {
        'store': {
            'items_available': fields.Integer(attribute='availability.store.items_available', default=4)
        }
    }
})
