import os
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

APPROVAL_TYPE = (
    ('approve', 'Diterima'),
    ('disallow', 'Ditolak'),
    ('further-discuss', 'Dibahas Lebih Lanjut'),
    ('no-status', 'Tanpa Status'),
)

AUTHORITIES_TYPE = (
    ('pusat', 'Pusat'),
    ('daerah', 'Daerah'),
    ('provinsi', 'Provinsi'),
    ('kabupaten', 'Kabupaten'),
    ('no-status', 'No Status'),
)

DOCUMENT_TYPE = (
    ('usulan', "Usulan"),
    ('audiensi', "Audiensi"),
)

FILE_EXTENSION_TYPE = (
    ('pdf', 'PDF'),
    ('excel', 'XLSX'),
    ('csv', 'CSV'),
    ('doc', 'DOCX'),
)

FILE_UPDATE_TYPE = (
    ('create', 'CREATE'),
    ('edit', 'EDIT'),
    ('delete', 'DELETE'),
    ('view', 'VIEW'),
)

FILE_CHANGED_TYPE = (
    ('FC1', 'Ubah Nama'),
    ('FC2', 'Salah File'),
    ('FC3', 'Ukuran File Besar'),
)

PROVINCE = (
    ('aceh', 'Aceh'),
    ('riau', 'Riau'),
    ('bengkulu', 'Bengkulu'),
    ('jawa Timur', 'Jawa Timur'),
    ('jambi', 'Jambi'),
    ('lampung', 'Lampung'),
    ('sumatera-selatan', 'Sumatera Selatan'),
    ('sumatera-barat', 'Sumatera Barat'),
    ('sumatera-utara', 'Sumatera Utara'),
    ('dki-jakarta', 'DKI Jakarta'),
    ('jawa-tengah', 'Jawa Tengah'),
    ('kepulauan-riau', 'Kepulauan Riau'),
    ('banten', 'Banten'),
    ('di-yogyakarta', 'DI Yogyakarta'),
    ('bangka-belitung', 'Bangka Belitung'),
    ('jawa-barat', 'Jawa Barat'),
    ('bali', 'Bali'),
)


class File(models.Model):

    file = models.FileField(verbose_name='Unggah File', null=False, blank=False)
    name = models.CharField(
                unique=True, verbose_name='Nama Dokumen',
                max_length=60, editable=False, null=False, blank=False)
    description = models.CharField(default="", verbose_name='Deskripsi Isi Dokumen', max_length=50)
    extension_type = models.CharField(choices=FILE_EXTENSION_TYPE, max_length=7, editable=False)
    document_type = models.CharField(choices=DOCUMENT_TYPE, max_length=13)
    uploaded_by = models.ForeignKey('app_login.User', on_delete=models.PROTECT)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    @property
    def get_file_name(self) -> str:
        filename: str = os.path.basename(self.file.name)
        return filename

    @property
    def get_file_extension(self) -> str:
        extension: str = self.get_file_name.split(".")[1]
        return extension

    def __str__(self) -> str:
        return '%s - %s' % (self.name, self.description)

    def get_absolute_url(self):
        return reverse("file", kwargs={"pk": self.pk})

    def save(self, force_insert: bool = False, force_update: bool = False, *args, **kwargs) -> None:
        self.name = self.get_file_name
        self.extension_type = self.get_file_extension
        return super(File, self).save(force_insert, force_update, *args, **kwargs)


class FileHistory(MPTTModel):

    file = models.OneToOneField('File', on_delete=models.RESTRICT)
    date_modified = models.DateTimeField(auto_now=True, editable=False)
    latest_status = models.CharField(default='no-status', choices=FILE_UPDATE_TYPE, max_length=19)
    description = models.CharField(choices=FILE_CHANGED_TYPE, verbose_name='Deskripsi Perubahan', max_length=30)
    parent = TreeForeignKey('self', related_name='LastModified', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.file, self.parent)

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})

    # def save(self, force_insert: bool = False, force_update: bool = False, *args, **kwargs) -> None:
    #     return super(FileHistory, self).save(force_insert, force_update, *args, **kwargs)


class Usulan(models.Model):

    nama = models.CharField(max_length=50, blank=False, null=False)
    provinsi = models.CharField(max_length=20, choices=PROVINCE, blank=False)
    kabkota = models.CharField(max_length=20, blank=False)
    nomor_usulan = models.CharField(max_length=30, blank=False)
    tanggal_usulan = models.DateTimeField()

    class Meta:
        abstract = True


class UsulanPemda(Usulan):

    judul_surat = models.CharField(max_length=50)
    jenis_surat = models.CharField(max_length=14)
    daftar_usulan_proyek = models.BooleanField(default=False)


class UsulanKlinik(Usulan):

    target = models.CharField(max_length=7)
    kebutuhan_anggaran = models.FloatField()
    lokasi = models.CharField(max_length=15)
    indikasi_tahun = models.CharField(max_length=5)
    kewenangan = models.CharField(choices=AUTHORITIES_TYPE, max_length=15)
    k_l_d = models.CharField(max_length=25)
    sektor = models.CharField(max_length=20)
    jenis_usulan = models.CharField(max_length=14)
    forum_perencanaan = models.CharField(max_length=8)
    dasar_usulan = models.CharField(max_length=10)
    kesepakatan = models.CharField(choices=APPROVAL_TYPE, max_length=15)
    keterangan = models.TextField()
    sumber_pendanaan = models.CharField(max_length=9)


class UsulanLanjut(Usulan):

    uraian_usulan = models.CharField(max_length=10)
    mekanisme_usulan = models.CharField(max_length=9)
    rekomendasi = models.TextField()
