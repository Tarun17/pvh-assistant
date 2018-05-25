"""
Module to handle data layer to performing CRUD for product item in DB
"""
from pvh_digital.api.es.connections import conn

class ProductNotFound(Exception):
    """
    Exception to handle product not found errors.
    """
    pass

def get_product(product_id):
    """
    Return a product
    :param product_id: ID  of the product (also known as GTIN/SKU/EAN/UPC)
    :return: Product
    """
    try:
        body = {
            "query": {
                "match": {
                    "id": product_id
                }
            }
        }
        response = conn.search(index='products', doc_type='products_type', body=body)
        hits = response.get('hits')
        total_found = hits.get('total')
        if total_found > 0:
            products = hits.get('hits')    
            product = products.pop()
            product = product.get('_source')
            return product
        else:
            message = 'Product with the given ID: {}, does not exist.'
            raise ProductNotFound(message.format(product_id))
    except Exception as runtime_exception:
        raise runtime_exception
