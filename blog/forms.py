from django import forms
from .models import Post, Categoria, Autor

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'resumen', 'contenido', 'precio', 'imagen', 'autor', 'categoria', 'activo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'resumen': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Resumen breve'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }