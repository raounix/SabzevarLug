from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import News,Author,Event


def MainPage(request):
    return render(request,"Dashboard/events_edit.html")

def News_Change(request):
    if(request.method == "POST"):
        text=request.POST['text']
        title=request.POST['title']
        slug=request.POST['slug']
        authors=Author.objects.all().filter(Author="raouf")
        news = News(Title=title,Slug=slug,Brief=text,MainText=text,author=authors[0])
        news.save()
        return HttpResponse("ok")
    elif(request.method =="GET"):
        return render(request,"Dashboard/news_edit.html")
def Events_Change(request):
    if(request.method == "POST"):
        text=request.POST['text']
        title=request.POST['title']
        slug=request.POST['slug']
        authors=Author.objects.all().filter(Author="raouf")
        news = Event(Title=title,Slug=slug,Brief=text,MainText=text,author=authors[0])
        news.save()
        return HttpResponse("ok")
    elif(request.method =="GET"):
        return render(request,"Dashboard/events_edit.html")