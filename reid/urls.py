from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('result/', views.upload_image_and_reid),
]