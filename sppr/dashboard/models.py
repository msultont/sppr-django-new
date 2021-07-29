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

# New Model Corresponding to Longlist and Shortlist Model


class DeputiId(models.Model):
    # Field name made lowercase.
    deputi_id = models.IntegerField(db_column='Deputi_ID', primary_key=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    nama_deputi = models.TextField(db_column='Nama Deputi')

    class Meta:
        managed = False
        db_table = 'Deputi_ID'

    def __str__(self) -> str:
        return self.nama_deputi


class DirektoratId(models.Model):
    # Field name made lowercase.
    direktorat_id = models.IntegerField(
        db_column='Direktorat_ID', primary_key=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    nama_direktorat = models.TextField(
        db_column='Nama Direktorat', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Direktorat_ID'

    def __str__(self) -> str:
        return self.nama_direktorat


class KlId(models.Model):
    # Field name made lowercase.
    kl_id = models.IntegerField(db_column='KL_ID', primary_key=True)
    nama = models.TextField(db_column='Nama')  # Field name made lowercase.
    # Field name made lowercase.
    singkatan = models.TextField(db_column='Singkatan', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KL_ID'

    def __str__(self) -> str:
        return f'{self.nama} ({self.singkatan})'


class KabupatenId(models.Model):
    # Field name made lowercase.
    provinsi_id = models.IntegerField(db_column='Provinsi_ID')
    # Field name made lowercase.
    kabupaten_id = models.IntegerField(
        db_column='Kabupaten_ID', primary_key=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    nama_kabupaten = models.TextField(db_column='Nama Kabupaten')

    class Meta:
        managed = False
        db_table = 'Kabupaten_ID'

    def __str__(self) -> str:
        return self.nama_kabupaten


class MajorprojectId(models.Model):
    # Field name made lowercase.
    mp_id = models.IntegerField(db_column='MP_ID', primary_key=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    nama_major_project = models.TextField(
        db_column='Nama Major Project', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MajorProject_ID'

    def __str__(self) -> str:
        return self.nama_major_project


class MitraId(models.Model):
    # Field name made lowercase.
    mitra_id = models.IntegerField(db_column='Mitra_ID', primary_key=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    nama_direktorat_mitra = models.TextField(db_column='Nama Direktorat Mitra')
    # Field name made lowercase.
    deputi = models.IntegerField(db_column='Deputi', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Mitra_ID'

    def __str__(self) -> str:
        return self.nama_direktorat_mitra


class ProvinsiId(models.Model):
    # Field name made lowercase.
    provinsi_id = models.IntegerField(
        db_column='Provinsi_ID', primary_key=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    nama_provinsi = models.TextField(
        db_column='Nama Provinsi', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Provinsi_ID'

    def __str__(self) -> str:
        return self.nama_provinsi


class ProyekId(models.Model):
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    nama_proyek = models.TextField(db_column='Nama Proyek')
    # Field name made lowercase.
    proyek_idd = models.IntegerField(db_column='Proyek_IDD', primary_key=True)

    class Meta:
        managed = False
        db_table = 'Proyek_ID'

    def __str__(self) -> str:
        return self.nama_proyek


class StatusId(models.Model):
    # Field name made lowercase.
    status_id = models.IntegerField(db_column='Status_ID', primary_key=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    nama_status = models.TextField(
        db_column='Nama Status', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Status_ID'

    def __str__(self) -> str:
        return self.nama_status


class SubtemaId(models.Model):
    # Field name made lowercase.
    sub_tema_id = models.IntegerField(
        db_column='Sub_Tema_ID', primary_key=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    subtema_rkp_2022 = models.TextField(
        db_column='Subtema RKP 2022', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SubTema_ID'

    def __str__(self) -> str:
        return self.subtema_rkp_2022


class SubditId(models.Model):
    # Field name made lowercase.
    subdit_id = models.IntegerField(db_column='Subdit_ID', primary_key=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    nama_subdit = models.TextField(
        db_column='Nama Subdit', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Subdit_ID'

    def __str__(self) -> str:
        return self.nama_subdit


class SumberdataId(models.Model):
    # Field name made lowercase.
    sumberdata_id = models.IntegerField(
        db_column='SumberData_ID', primary_key=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    nama_sumber = models.TextField(
        db_column='Nama Sumber', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SumberData_ID'

    def __str__(self) -> str:
        return self.nama_sumber


class TahapanId(models.Model):
    # Field name made lowercase.
    tahapan_id = models.IntegerField(db_column='Tahapan_ID', primary_key=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    nama_tahapan = models.TextField(
        db_column='Nama Tahapan', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tahapan_ID'

    def __str__(self) -> str:
        return self.nama_tahapan


class UserStatus(models.Model):
    # Field name made lowercase.
    user_status = models.IntegerField(
        db_column='User_Status', primary_key=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    nama_status = models.TextField(
        db_column='Nama Status', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User_Status'

    def __str__(self) -> str:
        return self.nama_status


class Longlist(models.Model):
    # ro_id = models.IntegerField(blank=True, null=True)
    provinsi = models.ForeignKey(
        'ProvinsiId', models.DO_NOTHING, db_column='provinsi', blank=True, null=True)
    judul_proyek = models.TextField(blank=True, null=False)
    # This field type is a guess.
    lokasi_proyek = models.TextField(blank=True, null=True)
    lokasi_kabupaten = models.ForeignKey(
        KabupatenId, models.DO_NOTHING, db_column='lokasi_kabupaten', blank=True, null=True)
    target_2021 = models.IntegerField(blank=True, null=True, default=0)
    target_2022 = models.IntegerField(blank=True, null=True, default=0)
    target_2023 = models.IntegerField(blank=True, null=True, default=0)
    target_2024 = models.IntegerField(blank=True, null=True, default=0)
    target_2025 = models.IntegerField(blank=True, null=True, default=0)
    indikasi_pendanaan_2021 = models.FloatField(
        blank=True, null=True, default=0)
    indikasi_pendanaan_2022 = models.FloatField(
        blank=True, null=True, default=0)
    indikasi_pendanaan_2023 = models.FloatField(
        blank=True, null=True, default=0)
    indikasi_pendanaan_2024 = models.FloatField(
        blank=True, null=True, default=0)
    sumber_data = models.ForeignKey(
        'SumberdataId', models.DO_NOTHING, db_column='sumber_data', blank=True, null=True)
    # Field name made lowercase.
    kl_pelaksana = models.ForeignKey(
        KlId, models.DO_NOTHING, db_column='KL_pelaksana', blank=True, null=True)
    shortlist_2022 = models.BooleanField(blank=True, null=True)
    shortlist_2023 = models.BooleanField(blank=True, null=True)
    isu_strategis = models.TextField(blank=True, null=True)
    # Field name made lowercase.
    tujuan_lfa = models.TextField(
        db_column='tujuan_LFA', blank=True, null=True)
    # Field name made lowercase.
    sasaran_lfa = models.TextField(
        db_column='sasaran_LFA', blank=True, null=True)
    # Field name made lowercase.
    output_lfa = models.TextField(
        db_column='output_LFA', blank=True, null=True)
    # Field name made lowercase.
    mp = models.ForeignKey('MajorprojectId', models.DO_NOTHING,
                           db_column='MP', blank=True, null=True)
    status_usulan = models.ForeignKey(
        'StatusId', models.DO_NOTHING, db_column='status_usulan', blank=True, null=True)
    sumber_bahasan = models.TextField(blank=True, null=True)
    taging_kawasan_prioritas = models.TextField(blank=True, null=True)
    jenis_project = models.ForeignKey(
        'ProyekId', models.DO_NOTHING, db_column='jenis_project', blank=True, null=True)
    sub_tema_rkp = models.ForeignKey(
        'SubtemaId', models.DO_NOTHING, db_column='sub_tema_rkp', blank=True, null=True)
    klasifikasi_proyek = models.TextField(blank=True, null=True)
    jenis_impact = models.TextField(blank=True, null=True)
    staging_perkembangan = models.TextField(blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    usulan_baru = models.BooleanField(blank=True, null=True)

    def __str__(self) -> str:
        return self.judul_proyek

    class Meta:
        managed = False
        db_table = 'Longlist'


class ShortList(models.Model):

    judul_proyek = models.OneToOneField(Longlist, on_delete=models.CASCADE)
    tahun_shortlist_2023 = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.judul_proyek
