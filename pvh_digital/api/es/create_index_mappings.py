"""
This script creates index mappings
"""

from pvh_digital.api.es.connections import conn

from pvh_digital.api.es.definitions import create_product_index_mappings
from pvh_digital.api.es.definitions import create_product_index_settings

create_product_index_settings(conn)
create_product_index_mappings(conn)
