from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Job
from .tasks import fetch_jobs

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job/job_list.html', {'jobs': jobs})

@login_required
def fetch_jobs_view(request):
    fetch_jobs.delay()  # Trigger the Celery task
    messages.success(request, 'Job fetching initiated successfully.')
    return redirect('job_list')
