import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

def fetch_jobs():
    url = "http://api.adzuna.com:80/v1/api/jobs/gb/search/1"
    params = {
        'app_id': settings.ADZUNA_APP_ID,
        'app_key': settings.ADZUNA_APP_KEY,
        'results_per_page': 20,
        'what': 'python-django developer',
        'what_exclude': 'java',
        'where': 'london',
        'sort_by': 'salary',
        'salary_min': 5000,
        'full_time': 1,
        'permanent': 1,
        'content-type': 'application/json'
    }
    response = requests.get(url, params=params)
    return response.json()

def job_list_view(request):
    jobs = fetch_jobs()
    return render(request, 'job/job_list.html', {'jobs': jobs})

def fetch_jobs_view(request):
    jobs = fetch_jobs()
    return JsonResponse(jobs)
