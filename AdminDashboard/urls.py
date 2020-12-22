from django.urls import path
from AdminDashboard import views

urlpatterns=[
    path("",views.MainPage),
    path("submit_post_change/",views.Submit_Post_Change),
]
