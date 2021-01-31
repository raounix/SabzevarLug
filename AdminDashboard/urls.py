from django.urls import path
from AdminDashboard import views
from .module import events,news
urlpatterns=[

    path("",views.MainPage),
    path("news/add/",news.News_Add),
    path("news/edit/",news.News_Edit),
    path("events/add/",events.Events_Add),
    path("events/edit/",events.Events_Edit),
    path("test/",views.test),
    path("login/",views.Login),
    path("logout/",views.Logout)
]
