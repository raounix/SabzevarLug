from django.urls import path
from AdminDashboard import views

urlpatterns=[
    path("",views.MainPage),
    path("news/add/",views.News_Change),
    path("events/add/",views.Events_Change),
    path("login/",views.Login),
    path("logout/",views.Logout)
]
