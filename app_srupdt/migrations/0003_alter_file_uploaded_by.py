# Generated by Django 3.2.14 on 2022-10-04 05:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_srupdt', '0002_auto_20221004_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
