from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.models import Event,Author

def Events_Add(request):
    if(request.user.is_authenticated==False):
        return redirect("/manage/login")
    else:

        if(request.method == "POST"):
            text=request.POST['text']
            title=request.POST['title']
            slug=request.POST['slug']
            authors=Author.objects.all().filter(Author="raouf")
            event = Event(Title=title,Slug=slug,Brief=text,MainText=text,author=authors[0])
            try:
                event.save()
                return HttpResponse("ok")
            except :
                return HttpResponse("error")
        elif(request.method =="GET"):
            return render(request,"Dashboard/events_add.html")




def Events_Edit(request):
    event= Event.objects.all()
    return render(request,"Dashboard/events_edit.html",{'event':event})

def Event_Edit_Post(request,slug):
    post = Event.objects.get(Slug=slug)
    return render(request,"Dashboard/edit_post.html",{'post':post,'type':'events'})



def update(request):
    
    post = Event.objects.get(Slug=request.POST['blog-edit-slug'])
    title=request.POST['blog-edit-title']
    main=request.POST['main_text']

    image =request.FILES['blogCustomFile']
    post.Title=title
    post.photo=image
    post.MainText=main
    try:
        post.save()
        return redirect("/manage/events/edit")
    except Exception as e:
        return HttpResponse(e.message)
