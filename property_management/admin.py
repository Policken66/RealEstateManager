from django.contrib import admin
from .models import PropertyListing, ViewingRequest, RentalAgreement
from .forms import PropertyListingForm, RentalAgreementForm

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

    # Добавление действия для подтверждения запроса
    actions = ['confirm_viewing_requests']

    def confirm_viewing_requests(self, request, queryset):
        updated = queryset.update(status='confirmed')
        self.message_user(request, f"Подтверждено {updated} запросов на просмотр.")
    confirm_viewing_requests.short_description = 'Подтвердить выбранные запросы'

@admin.register(RentalAgreement)
class RentalAgreementAdmin(admin.ModelAdmin):
    list_display = ('property_listing', 'client', 'start_date', 'end_date', 'signed_on')
    search_fields = ('client__username', 'property_listing__location')


class PropertyListingAdmin(admin.ModelAdmin):
    form = PropertyListingForm
    list_display = ('property_type', 'location', 'price', 'status')
    list_filter = ('status', 'property_type')
    search_fields = ('location', 'description')

class RentalAgreementalAdmin(admin.ModelAdmin):
    form = RentalAgreementForm
    list_display = ('property_listing', 'client', 'start_date', 'end_date')
    search_fields = ('client__username', 'property_listing__location')
    