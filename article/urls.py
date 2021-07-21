from django.contrib import admin
from django.urls import path
from article import views

app_name = "article"

urlpatterns = [
    path('mylist/<int:id>',views.mylist,name="mylist"),
    path('list/',views.list,name="list"),
    path('film/',views.film,name="film"),
    path('logout/',views.userlogout,name="logout"),
]