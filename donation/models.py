from django.db import models
from django.contrib.auth.models import User
from project.models import Project


class Donation(models.Model):
    donor = models.ForeignKey(User)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    project = models.ForeignKey(Project, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
