from django.db import models
from django.conf import settings

# Create your models here.

# Модель Объявлений о недвижимости
class PropertyListing(models.Model):
    STATUS_CHOICES = [
        ('available', 'Свободно'),
        ('rented', 'Сдано')
    ]

    property_type = models.CharField(max_length=50, verbose_name='Тип объекта')
    description = models.TextField(verbose_name='Описание объекта')
    area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Площадь (кв.м)")
    location = models.CharField(max_length=255, verbose_name='Местоположение')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена (руб.)')
    status = models.CharField(max_length=10, choices = STATUS_CHOICES, default = 'available', verbose_name='Статус')


    def __str__(self):
        return f"{self.property_type} - {self.location} ({self.get_status_display()})"
    
# Модель Запросов на просмотр
class ViewingRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидание'),
        ('confirmed', 'Подтверждаю'),
    ]

    property_listing = models.ForeignKey(PropertyListing, on_delete=models.CASCADE, related_name="viewing_requests", verbose_name="Объект")
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Клиент')
    requested_date = models.DateField(verbose_name='Дата просмотра')
    status = models.CharField(max_length=10, choices = STATUS_CHOICES, default = 'pending', verbose_name='Статус')

    def __str__(self):
        return f"Запрос на просмотр {self.property_listing} от {self.client.username}"
    
# Модель Договоров аренды
class RentalAgreement(models.Model):
    property_listing = models.ForeignKey(PropertyListing, on_delete=models.CASCADE, related_name='rental_agreements', verbose_name='Объект')
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Клиент')
    start_date = models.DateField(verbose_name='Дата начала аренды')
    end_date = models.DateField(verbose_name='Дата окончания аренды')
    signed_on = models.DateField(auto_now_add=True, verbose_name='Дата заключения договора')

    def __str__(self):
        return f"Договор аренды {self.property_listing} от {self.client.username}"