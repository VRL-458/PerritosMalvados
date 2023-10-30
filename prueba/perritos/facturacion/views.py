
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def factura(request):
    return render(request, 'facturacion.html')
