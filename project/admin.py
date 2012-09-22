from django.contrib import admin
from project.models import Project, Photo, Cause
from donation.admin import DonationInline

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0

class CauseAdmin(admin.ModelAdmin):
    model = Cause
    inlines = [PhotoInline]

class ProjectAdmin(admin.ModelAdmin):
    model = Project
    inlines = [DonationInline]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Cause, CauseAdmin)
