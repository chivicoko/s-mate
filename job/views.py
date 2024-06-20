import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.contrib import messages


def fetch_jobs(request):
    try:
        url = "http://api.adzuna.com:80/v1/api/jobs/gb/search/1"
        params = {
            'app_id': settings.ADZUNA_APP_ID,
            'app_key': settings.ADZUNA_APP_KEY,
            'results_per_page': 20,
            'what': 'python-django developer',
            'what_exclude': 'java',
            'where': 'Remote',
            'sort_by': 'salary',
            'salary_min': 5000,
            'content-type': 'application/json'
        }
        response = requests.get(url, params=params)
        return response.json()
    except:
        messages.error(request, 'Failed to fetch jobs. Please check your internet connection.')

def job_list_view(request):
    jobs = fetch_jobs(request)
    return render(request, 'job/job_list.html', {'jobs': jobs})

def fetch_jobs_view(request):
    jobs = fetch_jobs(request)
    return JsonResponse(jobs)
