from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('ser/', views.servicios),
    path('cotizacion/', views.cotizacion)

]