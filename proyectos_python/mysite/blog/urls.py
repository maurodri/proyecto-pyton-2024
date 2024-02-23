from django.urls import path
from . import views  # Importa tus vistas aquí

urlpatterns = [
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('course/', views.course, name='course'),
    path('single/', views.single, name='single'),
    path('teacher/', views.teacher, name='teacher'),
]
