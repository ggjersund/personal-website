"""
Journal application urls
"""
from django.urls import path
from . views import frontpage

app_name = 'journal'

urlpatterns = [
    path('', frontpage, name="index")
]
