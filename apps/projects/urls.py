"""
Projects application urls
"""
from django.urls import path
from . views import frontpage

app_name = 'projects'

urlpatterns = [
    path('', frontpage, name="index")
]
