# Generated by Django 4.2.2 on 2023-08-21 12:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('payment', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('currency', models.CharField(max_length=255)),
                ('date', models.DateField(default=datetime.date.today)),
                ('user', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default=0)),
                ('dealer_name', models.CharField(default='null', max_length=255)),
                ('client_name', models.CharField(default='null', max_length=255)),
                ('location', models.CharField(default='null', max_length=255)),
                ('order_price', models.IntegerField(default=0)),
                ('order_currency', models.CharField(default='null', max_length=255)),
                ('delivery', models.IntegerField(default=0)),
                ('delivery_currency', models.CharField(default='null', max_length=255)),
                ('final_amount', models.IntegerField(default=0)),
                ('remaining_amount', models.IntegerField(default=0)),
                ('items', models.CharField(default='null', max_length=1000)),
                ('date', models.DateField(default=datetime.date.today)),
                ('user', models.CharField(default='null', max_length=255)),
                ('status', models.CharField(default='Pending', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('admin', models.BooleanField(default=False)),
            ],
        ),
    ]