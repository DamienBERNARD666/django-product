from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    products=Product.objects.all()
    return render(request, 'index.html', {'products': products})

def product(request, id):
    pouet= Product.objects.get(id=id)
    return render(request, 'product.html', {'product': pouet})
