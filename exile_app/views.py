from django.shortcuts import render
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
    """Главная страница"""
    products = Products.objects.all()[:4] 
    
    context = {
        'products': products,
    }
    
    return render(request, 'index.html', context)