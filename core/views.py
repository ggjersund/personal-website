"""
Core views
"""
import socket
from django.shortcuts import render

def index(request):
    """
    Index view
    """
    return render(request, 'core/index.html', {'hostname': socket.gethostname()})
