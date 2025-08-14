from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Post, Categoria, Autor
from .forms import PostForm, CategoriaForm, AutorForm, BuscarForm

def index(request):
    posts = Post.objects.filter(activo=True)
    form = BuscarForm()
    context = {
        'posts': posts,
        'form': form,
        'titulo': 'Mi Blog Personal'
    }
    return render(request, 'blog/index.html', context)

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Post creado exitosamente!')
            return redirect('blog:index')
    else:
        form = PostForm()
    
    context = {
        'form': form,
        'titulo': 'Crear Nuevo Post',
        'accion': 'Crear'
    }
    return render(request, 'blog/crear_post.html', context)

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Categoría creada exitosamente!')
            return redirect('blog:index')
    else:
        form = CategoriaForm()
    
    context = {
        'form': form,
        'titulo': 'Crear Nueva Categoría',
        'accion': 'Crear'
    }
    return render(request, 'blog/crear_categoria.html', context)

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Autor creado exitosamente!')
            return redirect('blog:index')
    else:
        form = AutorForm()
    
    context = {
        'form': form,
        'titulo': 'Crear Nuevo Autor',
        'accion': 'Crear'
    }
    return render(request, 'blog/crear_autor.html', context)

def buscar_posts(request):
    posts = []
    query = ""
    
    if request.method == 'GET' and 'busqueda' in request.GET:
        form = BuscarForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['busqueda']
            posts = Post.objects.filter(
                Q(titulo__icontains=query) |
                Q(contenido__icontains=query) |
                Q(autor__nombre__icontains=query) |
                Q(categoria__nombre__icontains=query),
                activo=True
            )
    else:
        form = BuscarForm()
    
    context = {
        'form': form,
        'posts': posts,
        'query': query,
        'titulo': 'Buscar Posts'
    }
    return render(request, 'blog/buscar.html', context)
