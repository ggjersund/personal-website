"""
Core views
"""
import socket
from django.shortcuts import render

def frontpage(request):
    """
    Index view
    """
    return render(request, 'projects/projects.html', {'hostname': socket.gethostname()})
