# Generated by Django 3.0.8 on 2020-09-12 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_auto_20200912_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phone_number',
        ),
    ]
