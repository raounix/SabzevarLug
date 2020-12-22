from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def MainPage(request):
    return render(request,"Dashboard/post_editor.html")

def Submit_Post_Change(request):
    print(request.POST['text'])
    return HttpResponse("ok")