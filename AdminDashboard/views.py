from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth import authenticate, login,logout

def MainPage(request):
    if(request.user.is_authenticated ==False):
        return redirect("/manage/login")
    else:
        return render(request,"Dashboard/base.html")



def Login(request):
    if(request.method=="POST"):
        if(request.user.is_authenticated ==False):
            try:
                username=request.POST['username']
                password=request.POST['password']
                
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect("/manage")
            except:
                
                return HttpResponse("error")
        else:
            return HttpResponse("ok")
        
    elif (request.method=="GET"):
        if(request.user.is_authenticated ==False):
            return render(request,"Dashboard/login.html")
        else:
            return redirect("/manage")
        



def Logout(request):
    if(request.user.is_authenticated ):

        if(request.method=="GET"):
          
                logout(request)

                return redirect('/manage/login/')

            # return render(request,"Dashboard_Templates/login.html",{"login_status":"not_login"})
        else:
            return redirect('/manage/login/')
    else:
        return redirect('/manage/login/')



def test(request):
    return render(request,"Dashboard/edit_post.html")