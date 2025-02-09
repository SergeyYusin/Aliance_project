from django.db import models
from django.core.validators import MaxValueValidator
# from django import forms
# Create your models here.

PRODUCT_CONT = (
    ('Пульс Тепло', 'Пульс Тепло'),
    ('Пульс счетчик воды 80й', 'Пульс счетчик воды 80й'),
    ('Пульс счетчик воды 110й', 'Пульс счетчик воды 110й'),
    ('Пломбы', 'Пломбы')
)

DISTRICT = (
    ('САО', 'САО'),
    ('ЮАО', 'ЮАО'),
    ('ЗАО', 'ЗАО'),
    ('ВАО','ВАО')
)


class Person(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    product = models.CharField(max_length=50, choices=PRODUCT_CONT)
    quantity = models.IntegerField(validators=[MaxValueValidator(100)])
    date = models.DateField()

    def __str__(self):
        return f'{self.name} {self.last_name} Наименование: {self.product}, {self.quantity}шт.'


class Applications(models.Model):
    district = models.CharField(max_length=50, choices=DISTRICT)
    address = models.CharField(max_length=100)
    flat = models.IntegerField()
    phone = models.CharField(max_length=50)
    date = models.DateField()
    comment = models.TextField(max_length=100)
    price = models.IntegerField()
    uk = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return (f'{self.district} - {self.address} - {self.flat} - {self.phone} - {self.date} - {self.comment} - '
                f'{self.price} - {self.uk} - {self.comment}')
    class Meta:
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявки'

class MyModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)