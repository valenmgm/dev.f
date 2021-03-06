from django.forms import ModelForm
from . import models

class FormComentario(ModelForm):
    class Meta:
        model = models.Comment
        fields = ['autorcomment', 'comentario']

class FormPost(ModelForm):
    class Meta:
        model = models.Post
        fields = ['titulo', 'contenido', 'imagen', 'autor', 'categoria']

class FormCategoria(ModelForm):
    class Meta:
        model = models.Categoria
        fields = ['nombre_cat',]
