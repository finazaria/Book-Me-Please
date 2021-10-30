# Generated by Django 3.2.8 on 2021-10-28 08:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fina', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='book_interest',
            field=models.CharField(choices=[('Fiction', 'FICTION'), ('Non-Fiction', 'NON-FICTION'), ('Historical', 'HISTORICAL'), ('Biography', 'BIOGRAPHY'), ('Self-Development', 'SELF-DEVELOPMENT'), ('Business', 'BUSINESS')], default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='member_since',
            field=models.DateField(default=datetime.date(2021, 10, 28)),
        ),
    ]
