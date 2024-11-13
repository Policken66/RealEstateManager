# property_management/urls.py
from django.urls import path
from . import views

app_name = 'property_management' # Задаем пространство имен

urlpatterns = [
    path('', views.home, name='home'),

    # Главная страница каталога
    path('catalog/', views.catalog, name='catalog'),
    
    # Страница с деталями конкретного объекта
    path('property/<int:property_id>/', views.property_detail, name='property_detail'),
    
    # Страница с формой запроса на просмотр
    path('property/<int:property_id>/request/', views.viewing_request, name='viewing_request'),
    
    # Страница с формой заключения договора аренды
    path('property/<int:property_id>/rental_agreement/', views.rental_agreement, name='rental_agreement'),

    path('property/<int:property_id>/rent/', views.create_rental_agreement, name='create_rental_agreement'),

    path('property_list/', views.property_list, name='property_list'),
]