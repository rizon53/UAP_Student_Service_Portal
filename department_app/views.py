from django.shortcuts import render
from .models import DepartmentContact

def department_list(request):
    departments = DepartmentContact.objects.all()
    return render(request, 'department_list.html', {'departments': departments})