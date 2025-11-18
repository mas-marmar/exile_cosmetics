from django.shortcuts import render
from .models import *

def online(request):
    return render(request, 'index.html')

def products(request):
    product_number = int(request.GET.get('number', 2))
    
    products_from_db = Products.objects.all()[product_number - 1]
    
    return render(request, 'db.html', {
        'product': products_from_db  
    })
