from django.urls import path
from AdminDashboard import views
from .module import events,news
urlpatterns=[

    path("",views.MainPage),

    path("news/add/",news.News_Add),
    path("news/edit/",news.News_Edit),
    path("news/edit/<slug:slug>/",news.News_Edit_Post),
    path("post/update/",news.update),

    path("events/add/",events.Events_Add),
    path("events/edit/",events.Events_Edit),
    path("events/edit/<slug:slug>/",events.Event_Edit_Post),
    path("events/update/",events.update),

    path("login/",views.Login),
    path("logout/",views.Logout)
]
