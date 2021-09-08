from django.http.response import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

    #return HttpResponse("Hola")

def prueba1(request):
    documento='<http> <body> <h1> Página de prueba </h1></body> </http>'
    #return HttpResponse(documento)

    return render(request,'blog/prueba1.html',{'nombre':"omar", 'apellido':"Reissing"})