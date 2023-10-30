from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Servicios
def servicios(request):
    servicios = Servicios.objects.all()
    return render(request, 'servicios.html', {"servicios": servicios})

def cotizacion(request):
    return render(request, 'cotizacion.html', )
