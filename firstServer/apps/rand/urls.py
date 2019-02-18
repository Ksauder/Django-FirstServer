from django.urls import path, include
from apps.rand import views
urlpatterns = [
    path('', views.home, name="rand-home")
]