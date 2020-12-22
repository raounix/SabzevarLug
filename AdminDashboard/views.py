from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def MainPage(request):
    return render(request,"Dashboard/form-quill-editor.html")