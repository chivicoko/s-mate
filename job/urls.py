from django.urls import path
from .views import job_list, fetch_jobs_view

urlpatterns = [
    path('job_list/', job_list, name='job_list'),
    path('fetch-jobs/', fetch_jobs_view, name='fetch_jobs_view'),  # On-demand fetch URL
]
