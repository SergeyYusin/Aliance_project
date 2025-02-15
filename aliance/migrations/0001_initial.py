# Generated by Django 5.1.6 on 2025-02-06 13:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('product', models.CharField(choices=[('pulse_t', 'Пульс Тепло'), ('pulse_s_80', 'Пульс счетчик воды 80й'), ('pulse_s_110', 'Пульс счетчик воды 110й'), ('plomb', 'Пломбы')], max_length=50)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100)])),
                ('date_of_birth', models.DateField()),
            ],
        ),
    ]
