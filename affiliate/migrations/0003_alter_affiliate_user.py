# Generated by Django 4.1.4 on 2023-02-23 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('affiliate', '0002_affiliate_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliate',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]