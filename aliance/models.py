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


class Person(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    product = models.CharField(max_length=50, choices=PRODUCT_CONT)
    quantity = models.IntegerField(validators=[MaxValueValidator(100)])
    date = models.DateField()

    def __str__(self):
        return f'{self.name} {self.last_name} Наименование: {self.product}, {self.quantity}шт.'
    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склад'

