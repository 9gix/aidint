from django.contrib import admin
from project.models import Project, Photo, Cause

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0

class CauseAdmin(admin.ModelAdmin):
    model = Cause
    inlines = [PhotoInline]

class ProjectAdmin(admin.ModelAdmin):
    model = Project

admin.site.register(Project, ProjectAdmin)
admin.site.register(Cause, CauseAdmin)
