from django.urls import path
from app import views

urlpatterns=[
    path("",views.Home),
    path(r"calendar",views.Calendar),
    path(r"calendar/<slug:slug>",views.PostPage,name='PostPage'),
    path(r"events",views.PostPage,name='PostPage'),
    path(r"events/<slug:slug>",views.PostPage,name='PostPage'),
    path(r"news",views.News_Home,name='News_Home'),
    path(r"news/<slug:slug>",views.News_Post,name='News_Post'),
    path(r"topics",views.PostPage,name='PostPage'),
    path(r"topics/<slug:slug>",views.PostPage,name='PostPage'),
    path(r"speakers",views.PostPage,name='PostPage'),
    path(r"speakers/<slug:slug>",views.PostPage,name='PostPage'),
    path(r"images",views.Meet_Image,name='Meet_Image'),
    
]
