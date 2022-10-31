from django.urls import path

from image_app import views

urlpatterns = [
    path('<str:fk>/upload/', views.ImageView.as_view(), name='upload'),
    path('<str:fk>/display/', views.DisplayView.as_view(), name='display'),
]