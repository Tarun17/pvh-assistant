"""
Parsers for Search API's
"""

from flask_restplus import reqparse

arguments = reqparse.RequestParser()
arguments.add_argument('q', type=str, required=True, default=1, help='search keyword')
arguments.add_argument('sort_by', type=str, required=False, default=1, help='sort_by')
arguments.add_argument('filter', type=str, required=False, default=1, help='filter')
arguments.add_argument('page', type=int, required=False, default=1, help='Page number')
arguments.add_argument('offset', type=bool, required=False, default=0, help='offset')
arguments.add_argument('page_size', type=int, required=False, default=10, help='page_size')

