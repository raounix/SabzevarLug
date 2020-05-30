from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Post
# Create your views here.
from django.core import serializers
from .models import Post
import datetime

def MainPage (request):
    post = Post.objects.all()
    paginator = Paginator(post, 2) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    number = paginator.num_pages
    print(number)
    return render(request,"app_html/index.html",{'post':page_obj,'number':number})


def PostPage(request,slug):
    PostBlog = Post.objects.all().filter(Slug = slug)
   
    
    return render(request , "app_html/post.html",{'Postblog':PostBlog})
