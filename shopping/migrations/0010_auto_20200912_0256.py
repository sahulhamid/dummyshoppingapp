# Generated by Django 3.0.8 on 2020-09-12 09:56

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0009_profile_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]