from django.db import models
import os


class Cause(models.Model):
    caption = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.caption

def get_cause_image_path(instance, filename):
    return os.path.join('cause', str(instance.cause.id), filename)

class Photo(models.Model):
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_cause_image_path)
    cause = models.ForeignKey(Cause)

    def __unicode__(self):
        return self.caption


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    causes = models.ManyToManyField(Cause)
    budget = models.DecimalField(max_digits=16, decimal_places=2)
    begin_on = models.DateField()
    end_on = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
