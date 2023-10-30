from django.urls import path

from . import views

#URLConf
urlpatterns = [
    path('usr/', views.registro),
    path('login/', views.login),
    path('regitros/', views.registros, name='registro-u'),
    path('login2/', views.user_login, name='login')

]