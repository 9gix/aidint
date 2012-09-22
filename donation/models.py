from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class Donation(models.Model):
    donor = models.ForeignKey(User)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey("content_type", "object_id")
    created_at = models.DateTimeField(auto_now_add=True)
