# Generated by Django 3.2.4 on 2021-12-20 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_alter_tujuanlfa_nama_tujuan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outputlfa',
            name='pengaruh_output_sasaran',
        ),
        migrations.RemoveField(
            model_name='sasaranlfa',
            name='pengaruh_sasaran_tujuan',
        ),
    ]
