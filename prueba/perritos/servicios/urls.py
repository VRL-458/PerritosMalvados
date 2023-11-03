from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('ser/', views.servicios_view),
    path('cotizacion/', views.cotizacion),
    path('revisar_cotizaciones/', views.revisar_cotizaciones)
]