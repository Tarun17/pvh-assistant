"""
Database Initialization module
"""


def reset_database():
    """
    To Reset data
    :return: none
    """
    from pvh_digital.database.models import Item  # noqa
    Item.create_table(read_capacity_units=1, write_capacity_units=1)

