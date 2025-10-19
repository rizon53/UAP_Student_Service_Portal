from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'feedback_success.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})