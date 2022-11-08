import os
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Surat(models.Model):

    PIL_JENIS_SURAT = (
        ('usulan', "Penyampaian Usulan"),
        ('audiensi', "Permohonan Audiensi"),
    )

    PIL_PROVINSI = (
        ('11', 'Aceh'),
        ('12', 'Sumatera Utara'),
        ('13', 'Sumatera Barat'),
        ('14', 'Riau'),
        ('15', 'Jambi'),
        ('16', 'Sumatera Selatan'),
        ('17', 'Bengkulu'),
        ('18', 'Lampung'),
        ('19', 'Kep. Bangka Belitung'),
        ('21', 'Kep. Riau'),
        ('31', 'DKI Jakarta'),
        ('32', 'Jawa Barat'),
        ('33', 'Jawa Tengah'),
        ('34', 'DI Yogyakarta'),
        ('35', 'Jawa Timur'),
        ('36', 'Banten'),
        ('51', 'Bali'),
    )

    tautan_surat_masuk = models.CharField(max_length=400, null=True, blank=True)
    tanggal_surat = models.DateField(null=True, blank=True)
    nomor_surat = models.CharField(max_length=50, null=True, blank=True)
    judul_surat = models.CharField(max_length=300, null=True, blank=True)
    jenis_surat = models.CharField(choices=PIL_JENIS_SURAT, max_length=50, null=True, blank=True)
    provinsi = models.CharField(choices=PIL_PROVINSI, max_length=50, null=True, blank=True)
    kabupaten_kota = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.judul_surat + " - " + self.provinsi


class Audiensi(Surat):

    PIL_JENIS_USULAN = (
        ('infrastruktur', "Infrastruktur"),
        ('non infrastruktur', "Non infrastruktur"),
    )

    PIL_DASAR_USULAN = (
        ('audiensi', "Audiensi"),
        ('surat', "Surat"),
    )

    PIL_KEWENANGAN = (
        ('pusat', 'Pemerintah Pusat'),
        ('provinsi', 'Pemerintah Daerah Provinsi'),
        ('kabupaten/kota', 'Pemerintah Kabupaten/Kota'),
        ('swasta', 'Swasta'),
    )

    PIL_KRITERIA_USULAN = (
        ('usulan baru', 'Usulan Baru'),
        ('usulan lama', 'Usulan Lama'),
    )

    ket = "Kebutuhan anggaran (dalam juta rupiah)"
    kld = "Kementrian/Lembaga/Daerah"

    nomenklatur_usulan = models.CharField(max_length=300, null=True, blank=True)
    target_usulan = models.TextField(null=True, blank=True)
    kebutuhan_anggaran = models.IntegerField(null=True, blank=True, verbose_name=ket)
    indikasi_tahun_pembangunan = models.IntegerField(null=True, blank=True)
    lokasi_spesifik = models.CharField(max_length=50, null=True, blank=True)
    jenis_usulan = models.CharField(choices=PIL_JENIS_USULAN, max_length=100, null=True, blank=True)
    dasar_usulan = models.CharField(choices=PIL_DASAR_USULAN, max_length=20, null=True, blank=True)
    rc_pra_fs = models.BooleanField()
    rc_fs = models.BooleanField()
    rc_ded = models.BooleanField()
    rc_lahan = models.BooleanField()
    rc_amdal = models.BooleanField()
    tautan_rc = models.CharField(max_length=400, null=True, blank=True)
    catatan_readiness_criteria = models.TextField(null=True, blank=True)
    kewenangan = models.CharField(choices=PIL_KEWENANGAN, max_length=40, null=True, blank=True)
    kementerian_lembaga_daerah = models.CharField(max_length=300, null=True, blank=True, verbose_name=kld)
    sektor_bappenas = models.CharField(max_length=300, null=True, blank=True)
    kriteria_usulan = models.CharField(choices=PIL_KRITERIA_USULAN, max_length=100, null=True, blank=True)
    forum_perencanaan_pernah_diusulkan = models.BooleanField()
    tautan_risalah_audiensi = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.judul_surat + " - " + self.provinsi


class PenelaahanAwal(Audiensi):

    PIL_RPA = (
        ('tidak direkomendasikan', "Tidak Direkomendasikan"),
        ('dibahas lebih lanjut', "Dibahas Lebih Lanjut"),
    )

    ketersediaan_proyek_usulan = models.BooleanField()
    terdapat_nomenklatur_usulan_yang_jelas = models.BooleanField()
    terdapat_justifikasi_kebutuhan_usulan_proyek = models.BooleanField()
    terdapat_identifikasi_kewenangan_pusatdaerah_dari_usulan_proyek = models.BooleanField()
    memenuhi_kelengkapan_minimum_rediness_criteria = models.BooleanField()
    catatan_penelaahan_awal = models.TextField(null=True, blank=True)
    hasil_penelaahan_awal = models.CharField(choices=PIL_RPA, max_length=100, null=True, blank=True)

    def __str__(self):
        return self.judul_surat + " - " + self.provinsi


class KlinikKonsultasi(PenelaahanAwal):

    PIL_PENELAAHAN_AKHIR = (
        ('tidak direkomendasikan', "Tidak Direkomendasikan"),
        ('direkomendasikan', "Direkomendasikan"),
    )

    catatan_penelaahan_akhir = models.TextField(null=True, blank=True)
    indikasi_sumber_pendanaan = models.CharField(max_length=200, null=True, blank=True)
    hasil_penelaahan_akhir = models.CharField(choices=PIL_PENELAAHAN_AKHIR, max_length=100, null=True, blank=True)
    tautan_surat_jawaban = models.CharField(max_length=400, null=True, blank=True)
    tautan_nodin_laporan = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.judul_surat + " - " + self.provinsi


# APPROVAL_TYPE = (
#     ('approve', 'Diterima'),
#     ('disallow', 'Ditolak'),
#     ('further-discuss', 'Dibahas Lebih Lanjut'),
#     ('no-status', 'Tanpa Status'),
# )

# AUTHORITIES_TYPE = (
#     ('pusat', 'Pusat'),
#     ('daerah', 'Daerah'),
#     ('provinsi', 'Provinsi'),
#     ('kabupaten', 'Kabupaten'),
#     ('no-status', 'No Status'),
# )

# FILE_EXTENSION_TYPE = (
#     ('pdf', 'PDF'),
#     ('excel', 'XLSX'),
#     ('csv', 'CSV'),
#     ('doc', 'DOCX'),
# )

# FILE_UPDATE_TYPE = (
#     ('create', 'CREATE'),
#     ('edit', 'EDIT'),
#     ('delete', 'DELETE'),
#     ('view', 'VIEW'),
# )

# FILE_CHANGED_TYPE = (
#     ('FC1', 'Ubah Nama'),
#     ('FC2', 'Salah File'),
#     ('FC3', 'Ukuran File Besar'),
# )

# class File(models.Model):

#     file = models.FileField(verbose_name='Unggah File', null=False, blank=False)
#     name = models.CharField(
#                 unique=True, verbose_name='Nama Dokumen',
#                 max_length=60, editable=False, null=False, blank=False)
#     description = models.CharField(default="", verbose_name='Deskripsi Isi Dokumen', max_length=50)
#     extension_type = models.CharField(choices=FILE_EXTENSION_TYPE, max_length=7, editable=False)
#     document_type = models.CharField(choices=DOCUMENT_TYPE, max_length=13)
#     uploaded_by = models.ForeignKey('app_login.User', on_delete=models.PROTECT)
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     @property
#     def get_file_name(self) -> str:
#         filename: str = os.path.basename(self.file.name)
#         return filename

#     @property
#     def get_file_extension(self) -> str:
#         extension: str = self.get_file_name.split(".")[1]
#         return extension

#     def __str__(self) -> str:
#         return '%s - %s' % (self.name, self.description)

#     def get_absolute_url(self):
#         return reverse("file", kwargs={"pk": self.pk})

#     def save(self, force_insert: bool = False, force_update: bool = False, *args, **kwargs) -> None:
#         self.name = self.get_file_name
#         self.extension_type = self.get_file_extension
#         return super(File, self).save(force_insert, force_update, *args, **kwargs)


# class FileHistory(MPTTModel):

#     file = models.OneToOneField('File', on_delete=models.RESTRICT)
#     date_modified = models.DateTimeField(auto_now=True, editable=False)
#     latest_status = models.CharField(default='no-status', choices=FILE_UPDATE_TYPE, max_length=19)
#     description = models.CharField(choices=FILE_CHANGED_TYPE, verbose_name='Deskripsi Perubahan', max_length=30)
#     parent = TreeForeignKey('self', related_name='LastModified', on_delete=models.PROTECT)

#     def __str__(self):
#         return '%s - %s' % (self.file, self.parent)

#     def get_absolute_url(self):
#         return reverse("model_detail", kwargs={"pk": self.pk})

#     # def save(self, force_insert: bool = False, force_update: bool = False, *args, **kwargs) -> None:
#     #     return super(FileHistory, self).save(force_insert, force_update, *args, **kwargs)


# class Usulan(models.Model):

#     nama = models.CharField(max_length=50, blank=False, null=False)
#     provinsi = models.CharField(max_length=20, choices=PROVINCE, blank=False)
#     kabkota = models.CharField(max_length=20, blank=False)
#     nomor_usulan = models.CharField(max_length=30, blank=False)
#     tanggal_usulan = models.DateTimeField()

#     class Meta:
#         abstract = True


# class UsulanPemda(Usulan):

#     judul_surat = models.CharField(max_length=50)
#     jenis_surat = models.CharField(max_length=14)
#     daftar_usulan_proyek = models.BooleanField(default=False)


# class UsulanKlinik(Usulan):

#     target = models.CharField(max_length=7)
#     kebutuhan_anggaran = models.FloatField()
#     lokasi = models.CharField(max_length=15)
#     indikasi_tahun = models.CharField(max_length=5)
#     kewenangan = models.CharField(choices=AUTHORITIES_TYPE, max_length=15)
#     k_l_d = models.CharField(max_length=25)
#     sektor = models.CharField(max_length=20)
#     jenis_usulan = models.CharField(max_length=14)
#     forum_perencanaan = models.CharField(max_length=8)
#     dasar_usulan = models.CharField(max_length=10)
#     kesepakatan = models.CharField(choices=APPROVAL_TYPE, max_length=15)
#     keterangan = models.TextField()
#     sumber_pendanaan = models.CharField(max_length=9)


# class UsulanLanjut(Usulan):

#     uraian_usulan = models.CharField(max_length=10)
#     mekanisme_usulan = models.CharField(max_length=9)
#     rekomendasi = models.TextField()
