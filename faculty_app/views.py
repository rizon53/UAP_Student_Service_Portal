from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from student_app.models import StudentProfile
from marks_app.models import Marks

@login_required
def faculty_dashboard(request):
    students = StudentProfile.objects.all()
    return render(request, 'Fdashboard.html', {'students': students})


@login_required
def add_marks(request, student_id):
    student_profile = get_object_or_404(StudentProfile, id=student_id)

    if request.method == "POST":
        subject = request.POST.get('subject')
        ct1 = request.POST.get('ct1', 0)
        ct2 = request.POST.get('ct2', 0)
        ct3 = request.POST.get('ct3', 0)
        mid = request.POST.get('mid', 0)
        final = request.POST.get('final', 0)

        # ✅ Create Marks entry for this student
        Marks.objects.create(
            student=student_profile.user,
            subject=subject,
            ct1=ct1,
            ct2=ct2,
            ct3=ct3,
            mid=mid,
            final=final
        )

        return redirect('faculty_dashboard')

    return render(request, 'Fadd_marks.html', {'student': student_profile})