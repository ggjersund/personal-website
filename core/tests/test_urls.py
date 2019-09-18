"""
Core URL tests
"""

from django.urls import reverse, resolve


def test_index_url():
    """
    Test if index url is index
    """
    path = reverse('index')
    assert resolve(path).view_name == 'index'
