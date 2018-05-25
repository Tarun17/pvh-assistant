"""
Models module
"""

import pytz
import os
import boto3
from datetime import datetime
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection


class UserIndex(GlobalSecondaryIndex):
    """
    This class represents a global secondary index
    (for now not used because change in table strcuture)
    """
    class Meta(object):
        """
        Meta class for UserIndex
        """
        index_name = 'user-index'
        read_capacity_units = 1
        write_capacity_units = 1
        # All attributes are projected
        projection = AllProjection()

    user = UnicodeAttribute(default='', hash_key=True)


class Item(Model):
    """
    Model for Item
    """
    class Meta(object):
        """
        Meta Class for Item
        """
        table_name = os.environ.get('STAGE', 'dev') + '.item'
        region = boto3.Session().region_name
        host = 'http://localhost:8000' \
	        if not os.environ.get('LAMBDA_TASK_ROOT') else None
    user = UnicodeAttribute(hash_key=True)
    title = UnicodeAttribute()
    body = UnicodeAttribute()
    pub_date = UTCDateTimeAttribute(datetime.now(pytz.timezone('GMT')))
