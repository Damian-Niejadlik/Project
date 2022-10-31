from django.contrib import admin
from django.urls import path

from aplikacja import views

urlpatterns = [
    path('upload/', views.ImageView.as_view(), name='upload'),
    path('<str:fk>/display/', views.DisplayView.as_view(), name='display'),
]