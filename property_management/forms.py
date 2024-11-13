from django import forms
from .models import PropertyListing, RentalAgreement, ViewingRequest

class PropertyListingForm(forms.ModelForm):
    class Meta:
        model = PropertyListing
        fields = ['property_type', 'description', 'area', 'location', 'price', 'status']

class RentalAgreementForm(forms.ModelForm):
    class Meta:
        model = RentalAgreement
        fields = ['start_date', 'end_date']

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        if end_date and start_date and end_date <= start_date:
            raise forms.ValidationError("Дата окончания аренды должна быть позже даты начала.")
        return cleaned_data
    
class ViewingRequestForm(forms.ModelForm):
    class Meta:
        model = ViewingRequest
        fields = ['property_listing', 'requested_date']

    requested_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Дата просмотра')