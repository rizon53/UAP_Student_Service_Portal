from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.faculty_dashboard, name='faculty_dashboard'),
    path('add_marks/<int:student_id>/', views.add_marks, name='add_marks'),
]