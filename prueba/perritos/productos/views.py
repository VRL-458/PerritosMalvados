from django.shortcuts import render
from django.http import HttpResponse
import json


from .models import Categorias, Productos


# Create your views here.

def productos(request):
    productos = Productos.objects.all()
    return render(request, 'producto.html', {"productos":  productos})


