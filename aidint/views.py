from django.shortcuts import render
from project.models import Project
from donation.models import Donation
from django.contrib.auth.models import User

def index(request):
    projects = Project.objects.all()[:5]
    donations = Donation.objects.order_by('created_at')[:5]
    donors = User.objects.filter(userprofile__role='D')
    recipients = User.objects.filter(userprofile__role='R')
    return render(request, 'home.html', locals())
