from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def productos(request):

    with open('productos/static/datos/Productos.json', 'r') as archivo:
        data = json.load(archivo)



    return render(request, 'producto.html', {"productos":  data})
