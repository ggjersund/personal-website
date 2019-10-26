"""
Frontpage application urls
"""
from django.urls import path
from . views import frontpage

app_name = 'frontpage'

urlpatterns = [
    path('', frontpage, name="index")
]
