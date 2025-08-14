from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('crear-post/', views.crear_post, name='crear_post'),
    path('crear-categoria/', views.crear_categoria, name='crear_categoria'),
    path('crear-autor/', views.crear_autor, name='crear_autor'),
    path('buscar/', views.buscar_posts, name='buscar'),
]