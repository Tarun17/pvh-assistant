"""
Tests for Product API
"""

import pytest
from pvh_digital.app import app


@pytest.fixture
def client():
    """
    Client for testing API
    :return: Client
    """
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


def test_get_product(client):
    """
    Get an exiting product
    :param test_client:  client
    :return: test with 200 OK
    """
    resp = client.get('/api/product/11531002753')
    assert resp.status == '200 OK'


def test_get_nonexistent_product_int(client):
    """
    Get a non existent product
    :param test_client: client
    :return:  test with error 400 in response status
    """
    resp = client.get('/api/product/1234')
    assert '404' in resp.status


def test_get_nonexistent_product_str(client):
    """
    Get a non existent product
    :param test_client: client
    :return:  test with error 400 in response status
    """
    resp = client.get('/api/product/xyz')
    assert '404' in resp.status


def test_get_nonexistent_product_mixed(client):
    """
    Get a non existent product
    :param test_client: client
    :return:  test with error 400 in response status
    """
    resp = client.get('/api/product/xyz1234')
    assert '404' in resp.status
