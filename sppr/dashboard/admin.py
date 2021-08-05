from django.contrib import admin
from .models import CsvLongList, Endorsement, ListProvinsi, KementrianLembaga, KeteranganPrioritasNasional, Longlist, ShortList

# Register your models here.

admin.site.register(Endorsement)
admin.site.register(ListProvinsi)
admin.site.register(KementrianLembaga)
admin.site.register(KeteranganPrioritasNasional)
admin.site.register(Longlist)
admin.site.register(ShortList)
admin.site.register(CsvLongList)
