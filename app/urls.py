from django.urls import path
from app import views

urlpatterns=[
    path("",views.Home),
    path(r"calendar",views.Calendar_Content),
    path(r"events",views.Events_Home,name='Events_Home'),
    path(r"events/<slug:slug>",views.Events_Post,name='Events_Post'),
    path(r"news",views.News_Home,name='News_Home'),
    path(r"news/<slug:slug>",views.News_Post,name='News_Post'),
    path(r"topics",views.Topics_Home,name='Topics_Home'),
    path(r"topics/<slug:slug>",views.Topics_Post,name='Topics_Post'),
    path(r"speakers",views.Speakers_Home,name='Speakers_Home'),
    path(r"speakers/<slug:slug>",views.Speakers_Post,name='Speakers_Post'),
    path(r"images",views.Meet_Image,name='Meet_Image'),
    path(r"images/<slug:slug>",views.Meet_Image_Desc,name='Meet_Image_Desc')
    
]
