from django.urls import path

from . import views

#URLConf
urlpatterns = [
    path('carr/', views.carrito),
    path('eliminar_producto/<int:idProducto>/', views.eliminar_producto, name="eliminar_producto"),
    path('eliminar_carrito/', views.eliminar_carrito, name="eliminar_carrito"),
    path('eliminar_servicio/<int:idServicio>/', views.eliminar_servicio, name="eliminar_servicio")

]