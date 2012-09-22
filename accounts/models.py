from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    address = models.CharField(max_length=250)
    url = models.URLField()
    logo = models.ImageField(upload_to='company')

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    company = models.ForeignKey(Company, null=True, blank=True)
    bio = models.TextField()
    address = models.CharField(max_length=250)
    contact = models.CharField(max_length=25)
    role = models.CharField(max_length=1, choices=(('D', 'Donor'),('R','Recipient')))
