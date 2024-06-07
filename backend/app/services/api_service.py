"""
API service for data retrieval
"""

# Imports
from ..utils.db import get_test


def get_test_value(key):
    """Test retrieving values from the api endpoint

    Args:
        key (str): connectionn api key

    Returns:
        data: data retrieved from the api endpoint
    """
    return get_test(key)
