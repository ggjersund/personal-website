from django.test import TestCase
from django.urls import reverse, resolve

# Create your tests here.

def test_frontpage_url():
    path = reverse('frontpage:index')
    assert resolve(path).view_name == 'frontpage'
