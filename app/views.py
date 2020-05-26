from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.core import serializers
from .models import Post


def MainPage (request):
    post = Post.objects.all()
    return render(request,"app_html/index.html",{'post':post})
