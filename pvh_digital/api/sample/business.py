"""
Module to handle data layer to performing CRUD for item in DB
"""
#from pvh_digital.database import db
from pvh_digital.database.models import Item


def create_item(data):
    """
    Creating Data Item
    :param data: data needs to be created in DB
    :return: None
    """
    title = data.get('title')
    body = data.get('body')
    item = Item(title, body)
    # db.session.add(item)
    # db.session.commit()


def update_item(item_id, data):
    """
    Updating Data Item
    :param item_id: used as identifier to search record in db
    :param data: data required to be update
    :return: None
    """
    item = Item.query.filter(Item.id == item_id).one()
    item.title = data.get('title')
    item.body = data.get('body')
    # db.session.add(item)
    # db.session.commit()


def delete_item(item_id):
    """
    Deleting data item from DB
    :param item_id: used as identifier to search record in db
    :return:
    """
    post = Item.query.filter(Item.id == item_id).one()
    # db.session.delete(post)
    # db.session.commit()
