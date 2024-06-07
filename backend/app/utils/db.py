"""
Interact with postgres databse
"""

import psycopg2
from flask import current_app as app


def get_db_connection():
    """Connect to postgres database with psycopg2 wrapper

    Returns:
        connection: database connection to postgres db
    """
    return psycopg2.connect(app.config["DATABASE_URL"])


def get_test(key):
    """Test postgres database connection

    Returns:
        result: result from database query
    """
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            query = """
                SELECT value FROM test_table WHERE key = %s
            """
            cursor.execute(query, (key,))
            result = cursor.fetchone()
            if result:
                return result[0]
            return None
