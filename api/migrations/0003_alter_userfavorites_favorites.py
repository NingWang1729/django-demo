# Generated by Django 3.2.3 on 2021-05-16 23:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_user_favorites_userfavorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfavorites',
            name='favorites',
            field=models.CharField(blank=True, max_length=3600, validators=[django.core.validators.int_list_validator]),
        ),
    ]
