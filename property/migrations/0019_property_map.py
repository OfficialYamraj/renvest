# Generated by Django 4.1.4 on 2023-02-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_ipmodel_property_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='map',
            field=models.CharField(blank=True, max_length=5000),
        ),
    ]
