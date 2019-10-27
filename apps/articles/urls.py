"""
Articles application urls
"""
from django.urls import path
from . views import frontpage

app_name = 'articles'

urlpatterns = [
    path('', frontpage, name="index")
]
