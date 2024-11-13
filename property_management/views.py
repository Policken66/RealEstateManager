from django.shortcuts import render, get_object_or_404, redirect
from .models import PropertyListing, ViewingRequest, RentalAgreement
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import ViewingRequestForm, RentalAgreementForm
from django.contrib import messages

# Главная страница
def home(request):
    return render(request, 'property_management/home.html')

# Представление для отображения каталога объектов недвижимости
def catalog(request):
    listings = PropertyListing.objects.all()
    return render(request, 'property_management/catalog.html', {'listings': listings})

# Представление для отображения подробной информации о объекте
def property_detail(request, property_id):
    property_listing = get_object_or_404(PropertyListing, id=property_id)
    return render(request, 'property_management/property_detail.html', {'property': property_listing})

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

# Отображение доступных объектов недвижимости для клиентов

def property_list(request):
    # Отображаем только свободные объекты недвижимости
    available_properties = PropertyListing.objects.filter(status='available')
    return render(request, 'property_management/property_list.html', {'properties': available_properties})

@login_required
def property_detail(request, property_id):
    property = get_object_or_404(PropertyListing, id=property_id)
    if request.method == 'POST':
        form = ViewingRequestForm(request.POST)
        if form.is_valid():
            viewing_request = form.save(commit=False)
            viewing_request.client = request.user
            viewing_request.property_listing = property
            viewing_request.save()
            messages.success(request, "Запрос на просмотр отправлен.")
            return redirect('property_management:property_list')
    else:
        form = ViewingRequestForm()
    return render(request, 'property_management/property_detail.html', {'property': property, 'form': form})

@login_required
def create_rental_agreement(request, property_id):
    property = get_object_or_404(PropertyListing, id=property_id, status='available')
    if request.method == 'POST':
        form = RentalAgreementForm(request.POST)
        if form.is_valid():
            rental_agreement = form.save(commit=False)
            rental_agreement.client = request.user
            rental_agreement.property_listing = property
            rental_agreement.save()
            # Обновим статус объекта на "сдано"
            property.status = 'rented'
            property.save()
            messages.success(request, "Договор аренды успешно оформлен.")
            return redirect('property_management:property_list')
    else:
        form = RentalAgreementForm()
    return render(request, 'property_management/create_rental_agreement.html', {'property': property, 'form': form})