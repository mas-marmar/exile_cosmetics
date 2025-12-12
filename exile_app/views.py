from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Products

def search_view(request):
    query = request.GET.get('q', '').strip()
    
    if query:
        products = Products.objects.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query) |  
            Q(ingredients__icontains=query)  
        )
    else:
        products = Products.objects.none()  
    
    context = {
        'products': products,
        'query': query,
    }
    
    return render(request, 'search.html', context)

def index(request):
    products = Products.objects.all()[:4] 
    
    context = {
        'products': products,
    }
    
    return render(request, 'index.html', context)

def catalogue_view(request):
    products = Products.objects.all()
    
    product_id = request.GET.get('product')
    selected_product = None
    
    if product_id:
        try:
            selected_product = get_object_or_404(Products, id=product_id)
        except:
            selected_product = None
    
    context = {
        'products': products,
        'selected_product': selected_product,
    }
    return render(request, 'catalogue.html', context)