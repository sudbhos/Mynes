
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('', views.index,name="Index"),
    path("movieinfo",views.movieinfo,name="profile"),
    path("sportinfo",views.sportinfo,name="profile"),
    path("politicsinfo",views.politicsinfo,name="politicsinfo"),

]
