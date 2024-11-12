from django.shortcuts import render, get_object_or_404
from .models import PropertyListing, ViewingRequest, RentalAgreement
from django.http import HttpResponseRedirect
from django.urls import reverse

# Главная страница
def home(request):
    return render(request, 'home.html')

# Представление для отображения каталога объектов недвижимости
def catalog(request):
    listings = PropertyListing.objects.all()
    return render(request, 'property_management/catalog.html', {'listings': listings})

# Представление для отображения подробной информации о объекте
def property_detail(request, property_id):
    property_listing = get_object_or_404(PropertyListing, id=property_id)
    return render(request, 'property_management/property_detail.html', {'property_listing': property_listing})

# Представление для отправки запроса на просмотр
def viewing_request(request, property_id):
    property_listing = get_object_or_404(PropertyListing, id=property_id)
    
    if request.method == 'POST':
        requested_date = request.POST.get('requested_date')
        ViewingRequest.objects.create(
            property_listing=property_listing,
            client=request.user,
            requested_date=requested_date
        )
        return HttpResponseRedirect(reverse('catalog'))  # Перенаправляем на каталог после отправки запроса
    
    return render(request, 'property_management/viewing_request.html', {'property_listing': property_listing})

# Представление для заключения договора аренды
def rental_agreement(request, property_id):
    property_listing = get_object_or_404(PropertyListing, id=property_id)
    
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        RentalAgreement.objects.create(
            property_listing=property_listing,
            client=request.user,
            start_date=start_date,
            end_date=end_date
        )
        return HttpResponseRedirect(reverse('catalog'))  # Перенаправляем на каталог после создания договора
    
    return render(request, 'property_management/rental_agreement.html', {'property_listing': property_listing})