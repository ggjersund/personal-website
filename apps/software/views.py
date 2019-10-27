"""
Software views
"""
import socket
from django.shortcuts import render

def frontpage(request):
    """
    Index view
    """
    return render(request, 'software/software.html', {'hostname': socket.gethostname()})
