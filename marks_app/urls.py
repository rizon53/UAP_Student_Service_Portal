from django.urls import path
from . import views

urlpatterns = [
    path('', views.marks_list, name='marks_list'),
    path('add/', views.marks_add, name='marks_add'),
]