from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.models import News,Author

def News_Add(request):
    if(request.user.is_authenticated ==False):
        return redirect("/manage/login")
    else:
        if(request.method == "POST"):
            text=request.POST['text']
            title=request.POST['title']
            slug=request.POST['slug']
            authors=Author.objects.all().filter(Author="raouf")
            news = News(Title=title,Slug=slug,Brief=text,MainText=text,author=authors[0])
            try:
                news.save()
                return HttpResponse("ok")
            except :
                return HttpResponse("error")
        elif(request.method =="GET"):
            return render(request,"Dashboard/news_add.html")


def News_Edit(request):
    news = News.objects.all()
    return render(request,"Dashboard/news_edit.html",{'news':news})




def News_Edit_Post(request,slug):
    post = News.objects.get(Slug=slug)
    return render(request,"Dashboard/edit_post.html",{'post':post,'type':'post'})




def update(request):
    
    post = News.objects.get(Slug=request.POST['blog-edit-slug'])
    title=request.POST['blog-edit-title']
    main=request.POST['main_text']

    image =request.FILES['blogCustomFile']
    post.Title=title
    post.photo=image
    post.MainText=main
    try:
        post.save()
        return redirect("/manage/news/edit")
    except Exception as e:
        return HttpResponse(e.message)
