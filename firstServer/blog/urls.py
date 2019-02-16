from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('new', views.new, name="blog-new"),
    path('create', views.create, name="blog-create"),
    path('<number>/', views.show, name="blog-show")
]