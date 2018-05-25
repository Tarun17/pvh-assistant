"""
This module provides fuction for creaing index and creating mappings in Elasticsearch
"""

from pvh_digital.api.es.config import product_settings, product_mapping

def create_product_index_settings(conn):
    """
    This function creates the Index in ElasticSearch
    :rtype: json
    :return: status response
    """
    resp = conn.indices.create(index='products', body=product_settings)
    return resp


def create_product_index_mappings(conn):
    """
    This finction creates index mapping of existing Index
    :rtype: json
    :return: status response
    """
    resp = conn.indices.put_mapping(index='products', doc_type='default', body=product_mapping)
    return resp
