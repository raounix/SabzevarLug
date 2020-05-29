from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
from django.core import serializers
from .models import Post
import datetime

def MainPage (request):
    post = Post.objects.all()
    
    return render(request,"app_html/index.html",{'post':post})


def PostPage(request,slug):
    PostBlog = Post.objects.all().filter(Slug = slug)
   
    
    return render(request , "app_html/post.html",{'Postblog':PostBlog})
