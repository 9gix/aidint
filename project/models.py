from django.db import models
from imagekit.models.fields import ImageSpecField
from imagekit.processors.resize import ResizeToFit
import os


class Cause(models.Model):
    caption = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.caption

def get_cause_original_path(instance, filename):
    return os.path.join('cause', str(instance.cause.id), filename)

def get_cache_path(instance, path, specname, extension):
    filepath, basename = os.path.split(path)
    path, filedir = os.path.split(filepath)
    filename = os.path.splitext(basename)[0]
    new_name = '%s_%s%s' %(filename, specname, extension)
    return os.path.join('images', filedir, new_name)

class Photo(models.Model):
    caption = models.CharField(max_length=100)
    original = models.ImageField(upload_to=get_cause_original_path)
    thumbnail = ImageSpecField([ResizeToFit(100,100)], cache_to=get_cache_path,
            image_field='original', format='JPEG')
    preview = ImageSpecField([ResizeToFit(500,500)], cache_to=get_cache_path,
            image_field='original', format='JPEG')
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
