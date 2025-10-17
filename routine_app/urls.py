from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 👈 homepage
    path('routine_list/', views.routine_list, name='routine_list'),
]