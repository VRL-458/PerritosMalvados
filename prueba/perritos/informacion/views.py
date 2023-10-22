import json
from django.shortcuts import render


def info(request):
    # Cargar datos desde el archivo JSON
    with open('informacion/static/datos/Proyectos.json', 'r') as archivo:
        data = json.load(archivo)
    # Filtrar proyectos en proceso
    proyectos_en_proceso = [proyecto for proyecto in data if proyecto.get('EstadoProyecto') == 'En Proceso']
    # Pasar los proyectos en proceso a la plantilla
    return render(request, 'info.html', {'proyectos_en_proceso': data})
