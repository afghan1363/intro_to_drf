from django.db import models
from django.conf import settings


# Create your models here.
class Car(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', blank=True,
                              null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=1000.00, verbose_name='Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class Moto(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', blank=True,
                              null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мотоцикл'
        verbose_name_plural = 'Мотоциклы'


class Milage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True, related_name='milage')
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, null=True, blank=True, related_name='milage')

    milage = models.PositiveIntegerField(verbose_name='Пробег')
    year = models.PositiveSmallIntegerField(verbose_name='Год регистрации')

    def __str__(self):
        return f'{self.moto if self.moto else self.car} - {self.year}'

    class Meta:
        verbose_name = 'Пробег'
        verbose_name_plural = 'Пробеги'
        ordering = ('-year',)
