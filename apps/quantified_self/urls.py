"""
Quantified self application urls
"""
from django.urls import path
from . views import index

app_name = 'quantified_self'

urlpatterns = [
    path('', index, name="index")
]
