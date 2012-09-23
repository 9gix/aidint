from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

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

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
