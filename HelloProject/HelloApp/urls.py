from django.urls import path
from HelloApp import views

urlpatterns = [
    path("", views.home, name="home"),
]
