from django.shortcuts import render
import socket

def index(request):
    return render(request, 'core/index.html', {'hostname': socket.gethostname()})
