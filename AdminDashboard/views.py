from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import News,Author


def MainPage(request):
    return render(request,"Dashboard/post_editor.html")

def Submit_Post_Change(request):
    text=request.POST['text']
    title=request.POST['title']
    slug=request.POST['slug']
    authors=Author.objects.all().filter(Author="raouf")
    news = News(Title=title,Slug=slug,Brief=text,MainText=text,author=authors[0])
    news.save()
    return HttpResponse("ok")