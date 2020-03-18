from django.shortcuts import render

from .models import Job

def home(request):

    jobs = Job.objects   # this will gives us all the jobs that are in the db.

    return render(request, 'jobs/home.html', {'jobs':jobs})
