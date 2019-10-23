"""
Core URL tests
"""

from django.urls import reverse, resolve


def test_frontpage_url():
    """
    Test if index url is index
    """
    path = reverse('frontpage')
    assert resolve(path).view_name == 'frontpage'
