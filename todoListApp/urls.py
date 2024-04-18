from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    # TODO: Add tofoList to routing for views
     path("", views.home_page, name="todoList-home"), 
     path("test/", views.test, name="todoList-test"), 

]

