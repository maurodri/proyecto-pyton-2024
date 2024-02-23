from django.urls import path
from . import views  # Importa tus vistas aquí

urlpatterns = [
    path('', views.home_page, name='home_page'),
]
