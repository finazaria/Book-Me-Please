# Generated by Django 3.2.7 on 2021-11-05 02:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fina', '0005_alter_profile_member_since'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='member_since',
            field=models.DateField(default=datetime.date(2021, 11, 5)),
        ),
    ]
