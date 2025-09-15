from django.urls import path
from .views import (
    AboutView, PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView, MisPostsListView
)

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),               # alias a listado
    path('posts/', PostListView.as_view(), name='post_list'),
    path('about/', AboutView.as_view(), name='about'),
    path('posts/crear/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/editar/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/borrar/', PostDeleteView.as_view(), name='post_delete'),
    path('mis-posts/', MisPostsListView.as_view(), name='mis_posts'),
]