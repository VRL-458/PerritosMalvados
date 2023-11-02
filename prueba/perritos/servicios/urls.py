from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('ser/', views.servicios),
    path('cotizacion/', views.cotizacion),
    path('login_encargado/', views.encargado_login, name='login_encargado'),
    path('log3/', views.login_view_encargado),
    path('ver/', views.some_view)
]