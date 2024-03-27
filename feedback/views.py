from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save()
            return redirect('feedback_success', feedback_id=feedback.id)
    else:
        form = FeedbackForm()
        feedbacks = Feedback.objects.all().order_by('-created_at')
    return render(request, 'feedback.html', {'form': form, 'feedbacks': feedbacks})

def feedback_success(request, feedback_id):
    feedback = Feedback.objects.get(id=feedback_id)
    return render(request, 'success.html', {'feedback': feedback})