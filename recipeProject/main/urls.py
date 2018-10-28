from django.urls import path

from . import views

urlpatterns = [
    path('', views.recipes_index),
    path('recipes/<int:id>', views.recipes_detail),
]
