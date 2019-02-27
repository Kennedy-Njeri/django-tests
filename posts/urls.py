from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('posts', views.PostView.as_view(), name="posts"),

]