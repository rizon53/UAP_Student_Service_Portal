from django.shortcuts import render
from .models import Routine

def home(request):
    return render(request, 'home.html')


def routine_list(request):
    routines = None
    department = request.GET.get('department')
    year = request.GET.get('year')

    if department and year:
        routines = Routine.objects.filter(department=department, year=year)

    context = {
        'routines': routines,
        'departments': Routine._meta.get_field('department').choices,
        'years': Routine._meta.get_field('year').choices,
        'selected_dept': department,
        'selected_year': year,
    }
    return render(request, 'routine_list.html', context)