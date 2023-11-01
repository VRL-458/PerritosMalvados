from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('pro/', views.productos, name= 'productos'),
    path('productos/anadirCarrito/<int:idProducto>/', views.anadirCarrito, name='anadirCarrito'),

]