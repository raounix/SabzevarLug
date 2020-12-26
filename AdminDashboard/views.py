from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import News


def MainPage(request):
    return render(request,"Dashboard/post_editor.html")

def Submit_Post_Change(request):
    text=request.POST['text']
    title=request.POST['title']
    slug=request.POST['slug']
    news = News(Title=title,Slug=slug,Brief=text,MainText=text)
    news.save()
    return HttpResponse("ok")