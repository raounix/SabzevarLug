from django.urls import path
from app import views

urlpatterns=[
    path("",views.MainPage),
    path("test",views.PostPage),
    path('<slug:slug>',views.PostPage,name='PostPage'),
]
