from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from marks_app.models import Marks
from student_app.models import StudentProfile  # ✅ import this

def student_register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        department = request.POST.get('department', 'Not set')  # optional
        year = request.POST.get('year', 'Not set')

        # check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('student_register')

        # create new user
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        # ✅ Automatically create StudentProfile
        StudentProfile.objects.create(user=user, department=department, year=year)

        messages.success(request, "Registration successful! You can now login.")
        return redirect('login')

    return render(request, 'student_register.html')


@login_required
def student_dashboard(request):
    # Fetch marks for the logged-in student
    marks = Marks.objects.filter(student=request.user)
    return render(request, 'dashboard.html', {'marks': marks})