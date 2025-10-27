from django.shortcuts import render
from .models import *

def online(request):
    return render(request, 'index.html')
