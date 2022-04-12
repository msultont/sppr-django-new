from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin

# Register your models here.


class TujuanLFA_Admin(admin.ModelAdmin):
    list_display = ["nama_tujuan", "provinsi", "tahun", "indikator", "nilai"]


class SasaranLFA_Admin(admin.ModelAdmin):
    list_display = ["nama_sasaran", "tujuan", "indikator",
                    "nilai", "pengaruh_sasaran_tujuan"]


class OutputLFA_Admin(admin.ModelAdmin):
    list_display = ["nama_output", "sasaran", "indikator",
                    "nilai", "pengaruh_output_sasaran"]


class Longlist_Admin(admin.ModelAdmin):
    list_display = ["judul_proyek", "provinsi", "tahun_longlist"]


class SkoringProyek_Admin(admin.ModelAdmin):
    list_display = ["proyek", "nilai_raw_korelasi_sasaran",
                    "nilai_raw_korelasi_output", "nilai_raw_MP", "nilai_raw_investasi"]


admin.site.register(Longlist, Longlist_Admin)
admin.site.register(CsvLongList)
admin.site.register(DataKawasanPrioritas)
admin.site.register(SkoringProyek, SkoringProyek_Admin)
admin.site.register(TujuanLFA, TujuanLFA_Admin)
admin.site.register(SasaranLFA, SasaranLFA_Admin)
admin.site.register(OutputLFA, OutputLFA_Admin)
admin.site.register(NewIsuStrategis, MPTTModelAdmin)
admin.site.register(IsuStrategis, MPTTModelAdmin)