"""
Parser for Product API
"""

from flask_restplus import reqparse

# product arguments
product_arguments = reqparse.RequestParser()
product_arguments.add_argument('store_id', required=False, help='Store of the Associate')
