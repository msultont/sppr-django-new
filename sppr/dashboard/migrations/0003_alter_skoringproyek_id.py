# Generated by Django 3.2.4 on 2021-11-30 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_delete_hasilskoringproyek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skoringproyek',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
