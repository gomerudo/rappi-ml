"""Utility functions."""

import os
import mysql.connector
import rappiapp.app_config


def get_db_connection():
    """Returns a connector to a MySQL database.

    Parameters are read from the environment variables for security.
    """
    cnx = mysql.connector.connect(
        user=os.getenv(rappiapp.app_config.ENV_MYSQL_USER),  # 'rappi'
        password=os.getenv(rappiapp.app_config.ENV_MYSQL_PASSWORD),  # 'abc123'
        host='db',
        database=os.getenv(rappiapp.app_config.ENV_MYSQL_DATABASE)
    )
    return cnx
