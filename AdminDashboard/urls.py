from django.urls import path
from AdminDashboard import views

urlpatterns=[
    path("",views.MainPage),
    path("news_change/",views.News_Change),
    path("events_change/",views.Events_Change),
]
