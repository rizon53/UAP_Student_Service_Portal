from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def redirect_dashboard(request):
    user = request.user
    # check if user has a faculty profile
    if hasattr(user, 'facultyprofile'):
        return redirect('faculty_dashboard')
    # check if user has a student profile
    elif hasattr(user, 'studentprofile'):
        return redirect('student_dashboard')
    else:
        return redirect('home')  # fallback