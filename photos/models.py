from django.db import models


class Services(models.Model):
    name = models.CharField(max_length=100,verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Главная услуга'
        verbose_name_plural = 'Главные услуги'


class Subservices(models.Model):
    name = models.CharField(max_length=100,verbose_name='Название')
    image = models.FileField(upload_to='services_image', verbose_name='Картинка')
    basic_service = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='Главная услуга')
    description = models.TextField(max_length=700, verbose_name='Описание', blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class Example_photos(models.Model):
    name = models.CharField(max_length=100,verbose_name='Название')
    image = models.FileField(upload_to='example_image', verbose_name='Картинка')
    basic_subservice = models.ForeignKey(Subservices, on_delete=models.CASCADE, verbose_name='Услуга')
    description = models.TextField(max_length=500, verbose_name='Описание', blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пример'
        verbose_name_plural = 'Примеры'

