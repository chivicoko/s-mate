import requests
from django.core.management.base import BaseCommand
from django.conf import settings
from blogapp.models import Job

class Command(BaseCommand):
    help = 'Fetch jobs from Adzuna API'

    def handle(self, *args, **kwargs):
        url = f"http://api.adzuna.com:80/v1/api/jobs/gb/search/1?app_id={settings.ADZUNA_APP_ID}&app_key={settings.ADZUNA_APP_KEY}&results_per_page=20&what=python-django%20developer&what_exclude=java&where=london&sort_by=salary&salary_min=5000&full_time=1&permanent=1&content-type=application/json"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for job in data['results']:
                Job.objects.update_or_create(
                    title=job['title'],
                    company=job['company']['display_name'],
                    location=job['location']['display_name'],
                    description=job['description'],
                    salary_min=job['salary_min'],
                    salary_max=job['salary_max'],
                    redirect_url=job['redirect_url'],
                )
            self.stdout.write(self.style.SUCCESS('Successfully fetched and saved jobs'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch jobs'))
