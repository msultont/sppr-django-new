from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Endorsement(models.Model):
    id = models.IntegerField(primary_key=True)
    provinsi = models.ForeignKey('ListProvinsi', models.CASCADE)
    urutan = models.IntegerField()
    nama_kegiatan = models.TextField()
    satuan = models.TextField(blank=True, null=True)
    pn = models.ForeignKey('KeteranganPrioritasNasional', models.CASCADE)
    major_project = models.TextField(blank=True, null=True)
    lokasi = models.TextField(blank=True, null=True)
    ki = models.ForeignKey('KementrianLembaga', models.CASCADE)
    direktorat_mitra = models.TextField(blank=True, null=True)
    rakorgub = models.BooleanField(blank=True, null=True)
    rakortek = models.BooleanField(blank=True, null=True)
    musrenbangnas = models.BooleanField(blank=True, null=True)
    rakortekbang = models.BooleanField(blank=True, null=True)
    status_approval = models.TextField(blank=True, null=True)
    ket_approval = models.TextField(blank=True, null=True)
    vol = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nama_kegiatan

    class Meta:
        managed = False
        db_table = 'endorsement'


class KementrianLembaga(models.Model):
    id = models.IntegerField(primary_key=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    nama_kementrian_lembaga = models.TextField(
        db_column='Nama Kementrian Lembaga', blank=True, null=True)

    def __str__(self):
        return self.nama_kementrian_lembaga

    class Meta:
        managed = False
        db_table = 'kementrian_lembaga'


class KeteranganPrioritasNasional(models.Model):
    # Field renamed to remove unsuitable characters.
    keterangan_prioritas_nasional = models.TextField(
        db_column='keterangan prioritas nasional', blank=True, null=True)

    def __str__(self):
        return self.keterangan_prioritas_nasional

    class Meta:
        managed = False
        db_table = 'keterangan_prioritas_nasional'


class ListProvinsi(models.Model):
    id = models.IntegerField(primary_key=True)
    prov_id = models.IntegerField(blank=True, null=True)
    nama_provinsi = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nama_provinsi

    class Meta:
        managed = False
        db_table = 'list_provinsi'
