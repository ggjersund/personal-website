"""
Software application urls
"""
from django.urls import path
from . views import frontpage

app_name = 'software'

urlpatterns = [
    path('', frontpage, name="index")
]
