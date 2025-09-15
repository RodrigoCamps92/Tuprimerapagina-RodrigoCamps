from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from .models import Post
from .forms import PostForm

class AboutView(TemplateView):
    template_name = 'blog/about.html'

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        qs = Post.objects.filter(activo=True).select_related('autor', 'categoria')
        q = self.request.GET.get('q', '').strip()
        if q:
            qs = qs.filter(
                Q(titulo__icontains=q) |
                Q(resumen__icontains=q) |
                Q(contenido__icontains=q) |
                Q(categoria__nombre__icontains=q) |
                Q(autor__nombre__icontains=q) |
                Q(autor__apellido__icontains=q)
            )
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['titulo'] = 'Mi Blog Django'
        ctx['q'] = self.request.GET.get('q', '')
        return ctx

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        messages.success(self.request, '¡Post creado correctamente!')
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        messages.success(self.request, '¡Post actualizado!')
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Post eliminado.')
        return super().delete(request, *args, **kwargs)

class MisPostsListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Criterio simple: empareja email del Autor con el email del usuario
        return Post.objects.filter(activo=True, autor__email=self.request.user.email)