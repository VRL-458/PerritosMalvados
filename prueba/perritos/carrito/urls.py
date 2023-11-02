from django.urls import path

from . import views

#URLConf
urlpatterns = [
    path('carr/', views.carrito),
    path('carr/eliminarproducto/<int:idProducto>/', views.eliminar_producto, name="eliminar_produducto")

]