from django.urls import path

from . import views

#URLConf
urlpatterns = [
    path('usr/', views.registro),
    path('login/', views.login_view),
    path('venta/', views.ventas),
    path('perfil/', views.perfil),
    path('regitros/', views.registros, name='registro-u'),
    path('login2/', views.user_login, name='login'),
    path('ver/', views.some_view),
    path('procesar-compra/', views.procesar_compra, name='procesar_compra'),
    path('factura/<int:factura_id>/', views.factura, name='factura'),

]