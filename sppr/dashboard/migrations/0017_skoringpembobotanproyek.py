# Generated by Django 3.2.4 on 2021-11-26 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_auto_20211027_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkoringPembobotanProyek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nilai_korelasi_sasaran', models.FloatField(blank=True, null=True)),
                ('nilai_korelasi_output', models.FloatField(blank=True, null=True)),
                ('nilai_MP', models.FloatField(blank=True, null=True)),
                ('nilai_investasi', models.FloatField(blank=True, null=True)),
                ('nama_proyek', models.ForeignKey(blank=True, db_column='longlist', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.longlist')),
            ],
        ),
    ]
