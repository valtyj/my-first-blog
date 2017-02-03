from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts': posts})

def index(request):
    response = HttpResponse()
    response.write("<h1>Blog</h1><hr>")
    return response

def viewArticle(request, article_id):
    text = "Displaying article Number: %s" %article_id
    return HttpResponse(text)
