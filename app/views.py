from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Post,News,Images_Info,Images,Calendar,Event,Author
# Create your views here.
from django.core import serializers
from .models import Post
from django import template
import datetime
from os.path import splitext

def Home (request):
    news = News.objects.filter(Status='p')
    events=Event.objects.filter(Status='p')
    news_paginator = Paginator(news,5) # Show 25 contacts per page.
    events_paginator = Paginator(events,5) # Show 25 contacts per page.


  
    
    page_obj = news_paginator.get_page(1)
    
    number = news_paginator.num_pages
    

    return render(request,"app_html/home.html",{'post':page_obj,'events':events,'number':number})





# register = template.Library()


# @register.filter
# def noext(value):
#     return splitext(value)[0]

def Calendar_Content(request):
    contents = Calendar.objects.all()
    return render(request , "app_html/calendar.html",{"contents":contents})


def News_Home(request):
    news = News.objects.filter(Status='p')
    paginator = Paginator(news,5) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    
    
    page_obj = paginator.get_page(page_number)
    number = paginator.num_pages
    

    return render(request,"app_html/news.html",{'news':page_obj,'number':number})

def News_Post(request,slug):
    news = News.objects.all().filter(Slug = slug,Status='p')


    return render(request,"app_html/news_post.html",{'news':news})

################################################################################################
#Meet

def Meet_Image(request):
    image=Images_Info.objects.all()
    paginator = Paginator(image,5)
    page_obj = paginator.get_page(1)

    return render(request,"app_html/meet_image.html",{'images':page_obj})




def Meet_Image_Desc(request,slug):
    selected_post=Images_Info.objects.all().filter(Slug=slug)
    other_image = Images.objects.filter(image_rel__in=selected_post)
    
    

    return render(request,"app_html/meet_image_desc.html",{'images':selected_post,'other_image':other_image})
################################################################################################
#Event

def Events_Home(request):
    events = Event.objects.filter(Status='p')
    paginator = Paginator(events,5) # Show 25 contacts per page.

    page_number = request.GET.get('page')
  
    
    page_obj = paginator.get_page(page_number)
    number = paginator.num_pages
    

    return render(request,"app_html/events.html",{'events':page_obj,'number':number})

def Events_Post(request,slug):

    event = Event.objects.all().filter(Slug = slug,Status='p')

    return render(request,"app_html/events_post.html",{'events':event})

################################################################################################

def Topics_Home(request):
    topic = Event.objects.only('Issue')
    return render(request,"app_html/topics.html",{'topics':topic})

def Topics_Post(request,slug):
    topic = Event.objects.all().filter(Issue=slug,Status='p')
    print(topic)
    return render(request,"app_html/topics_post.html",{'topics':topic})

################################################################################################
def Speakers_Home(request):
    speakers = Author.objects.all()
    return render(request,"app_html/speakers.html",{'speakers':speakers})

def Speakers_Post(request,slug):
    authors=Author.objects.all().filter(Author=slug)
    speakers = Event.objects.all().filter(author__in=authors)
    return render(request,"app_html/speakers_post.html",{'speakers':speakers,'author':slug})