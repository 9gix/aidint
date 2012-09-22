from django.contrib import admin
from donation.models import Donation
from django.contrib.contenttypes import generic

class DonationInline(generic.GenericTabularInline):
    model = Donation
    extra = 0
