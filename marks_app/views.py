from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Marks
from .forms import MarksForm
from django.contrib.auth.decorators import login_required

@login_required
def marks_list(request):
    marks = Marks.objects.filter(student=request.user)
    return render(request, 'marks_list.html', {'marks': marks})

@login_required
def marks_add(request):
    if request.method == 'POST':
        form = MarksForm(request.POST)
        if form.is_valid():
            m = form.save(commit=False)
            m.student = request.user
            m.save()
            return redirect('/marks/')
    else:
        form = MarksForm()
    return render(request, 'marks_add.html', {'form': form})