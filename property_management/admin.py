from django.contrib import admin
from .models import PropertyListing, ViewingRequest, RentalAgreement

@admin.register(PropertyListing)
class PropertyListingAdmin(admin.ModelAdmin):
    list_display = ('property_type', 'location', 'price', 'status')
    list_filter = ('status', 'property_type')
    search_fields = ('location', 'property_type')

@admin.register(ViewingRequest)
class ViewingRequestAdmin(admin.ModelAdmin):
    list_display = ('property_listing', 'client', 'requested_date', 'status')
    list_filter = ('status', 'requested_date')
    search_fields = ('client__username', 'property_listing__location')

@admin.register(RentalAgreement)
class RentalAgreementAdmin(admin.ModelAdmin):
    list_display = ('property_listing', 'client', 'start_date', 'end_date', 'signed_on')
    list_filter = ('start_date', 'end_date')
    search_fields = ('client__username', 'property_listing__location')