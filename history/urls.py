from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('history/', views.history_view, name='history'),
]