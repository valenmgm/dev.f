from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse_lazy, reverse
#
from . import models
from . import forms
# Create your views here.

def index(request):
    publicacion = models.Post.objects.all()
    infocategorias = models.Categoria.objects.all()
    return render(request, 'index.html', {'datos': publicacion, 'categorias':infocategorias})

@csrf_exempt
def detail(request, idp):
    infopost = models.Post.objects.get(pk = idp)
    infocomments = models.Comment.objects.filter(posteado__id = idp)#post_id = pk
    form = forms.FormComentario()

    if request.method =='POST':
        formset = forms.FormComentario(request.POST)
        if formset.is_valid():
            data = formset.cleaned_data
            comentario = data['comentario']
            autorcomment = data['autorcomment']
            posteado = infopost

            nuevo = models.Comment()
            nuevo = nuevo.make(comentario, autorcomment, posteado)
            nuevo.save()

    return render(request, 'detail.html', {"datospost":infopost, "datoscomment":infocomments, "formfill":form})

def categoria(request, idcat):
    posts_de_categoria = models.Post.objects.filter(categoria = idcat)
    infocategoria = models.Post.objects.get(pk = idcat)
    return render(request, 'porcategoria.html', {'datapost':posts_de_categoria, 'datacat':infocategoria})


@csrf_exempt
def newpost(request):
    formNP = forms.FormPost()
    if request.method == 'POST':
        formset = forms.FormPost(request.POST)
        if formset.is_valid():
            data = formset.cleaned_data
            titulo = data['titulo']
            contenido = data['contenido']
            imagen = data['imagen']
            autor = data['autor']
            categoria = data['categoria']

            nuevopost = models.Post()
            nuevopost = nuevopost.make(titulo, contenido, imagen, autor, categoria)
            nuevopost.save()

            idnew = models.Post.objects.latest('fechal')
            return redirect('detalle', idnew.id)

    return(render(request, 'newpost.html', {'formfill':formNP}))
