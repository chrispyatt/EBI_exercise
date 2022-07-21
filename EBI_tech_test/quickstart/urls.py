from django.urls import path
from quickstart import views
from .views import HomePageView
from django.contrib import admin

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]