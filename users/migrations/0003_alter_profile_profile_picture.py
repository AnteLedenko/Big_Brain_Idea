# Generated by Django 4.2.16 on 2025-02-15 18:24

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(default='default', max_length=255, verbose_name='image'),
        ),
    ]
