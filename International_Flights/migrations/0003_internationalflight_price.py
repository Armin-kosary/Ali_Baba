# Generated by Django 5.0.6 on 2024-06-16 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('International_Flights', '0002_rename_internalflight_internationalflight'),
    ]

    operations = [
        migrations.AddField(
            model_name='internationalflight',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]