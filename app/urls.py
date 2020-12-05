from django.urls import path
from app import views

urlpatterns=[
    path("",views.Home),
    path(r"calendar",views.Calendar_Content),
    path(r"events",views.Events_Home,name='Events_Home'),
    path(r"events/<slug:slug>",views.Events_Post,name='Events_Post'),
    path(r"news",views.News_Home,name='News_Home'),
    path(r"news/<slug:slug>",views.News_Post,name='News_Post'),
    path(r"topics",views.PostPage,name='PostPage'),
    path(r"topics/<slug:slug>",views.PostPage,name='PostPage'),
    path(r"speakers",views.PostPage,name='PostPage'),
    path(r"speakers/<slug:slug>",views.PostPage,name='PostPage'),
    path(r"images",views.Meet_Image,name='Meet_Image'),
    path(r"images/<slug:slug>",views.Meet_Image_Desc,name='Meet_Image_Desc')
    
]
