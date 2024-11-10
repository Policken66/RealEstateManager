from django.contrib import admin
from .models import PropertyListing, ViewingRequest, RentalAgreement

admin.site.register(PropertyListing)
admin.site.register(ViewingRequest)
admin.site.register(RentalAgreement)

