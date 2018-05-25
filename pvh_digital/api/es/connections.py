"""
This module creates a elasticserach connection
"""
import elasticsearch

from .config import ES_HOST

conn = elasticsearch.Elasticsearch([ES_HOST])
