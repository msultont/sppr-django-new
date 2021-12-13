from django.contrib import admin
from .models import CsvLongList, DataKawasanPrioritas, IsuStrategis, Longlist, OutputLFA, SasaranLFA, SkoringProyek, TujuanLFA
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin

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


admin.site.register(Longlist, Longlist_Admin)
admin.site.register(CsvLongList)
admin.site.register(DataKawasanPrioritas)
admin.site.register(SkoringProyek)
admin.site.register(TujuanLFA, TujuanLFA_Admin)
admin.site.register(SasaranLFA, SasaranLFA_Admin)
admin.site.register(OutputLFA, OutputLFA_Admin)
admin.site.register(
    IsuStrategis,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
)
