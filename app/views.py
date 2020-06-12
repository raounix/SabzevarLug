from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Post
# Create your views here.
from django.core import serializers
from .models import Post
from django import template
import datetime
from os.path import splitext

def MainPage (request):
    post = Post.objects.filter(Status='p')
    paginator = Paginator(post, 3) # Show 25 contacts per page.

    page_number = request.GET.get('page')
  
    
    page_obj = paginator.get_page(page_number)
    number = paginator.num_pages
    

    return render(request,"app_html/index.html",{'post':page_obj,'number':number})


def PostPage(request,slug):
    PostBlog = Post.objects.all().filter(Slug = slug)

   
    
    return render(request , "app_html/post.html",{'Postblog':PostBlog})



register = template.Library()


@register.filter
def noext(value):
    return splitext(value)[0]