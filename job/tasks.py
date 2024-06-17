from celery import shared_task
import requests
from django.conf import settings
from .models import Job

@shared_task
def fetch_jobs():
    url = f"http://api.adzuna.com:80/v1/api/jobs/gb/search/1?app_id={settings.ADZUNA_APP_ID}&app_key={settings.ADZUNA_APP_KEY}&results_per_page=20&what=python-django%20developer&what_exclude=java&where=london&sort_by=salary&salary_min=5000&full_time=1&permanent=1&content-type=application/json"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for job in data['results']:
            Job.objects.update_or_create(
                title=job['title'],
                defaults={
                    'company': job['company']['display_name'],
                    'location': job['location']['display_name'],
                    'description': job['description'],
                    'salary_min': job['salary_min'],
                    'salary_max': job['salary_max'],
                    'redirect_url': job['redirect_url'],
                }
            )
    else:
        print(f"Failed to fetch jobs: {response.status_code}")
