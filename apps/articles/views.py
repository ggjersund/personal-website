"""
Articles views
"""
import socket
from django.shortcuts import render

def frontpage(request):
    """
    Index view
    """
    return render(request, 'articles/articles.html', {'hostname': socket.gethostname()})
