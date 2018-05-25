from flask_restplus import fields
from pvh_digital.api.restplus import api

item = api.model('Item', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a sample item'),
    'title': fields.String(required=True, description=' title'),
    'body': fields.String(required=True, description=' content'),
    'pub_date': fields.DateTime
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_items = api.inherit('Page of sample items', pagination, {
    'items': fields.List(fields.Nested(item))
})
