from django.contrib import admin
from .models import Endorsement, ListProvinsi, KementrianLembaga, KeteranganPrioritasNasional

# Register your models here.

admin.site.register(Endorsement)
admin.site.register(ListProvinsi)
admin.site.register(KementrianLembaga)
admin.site.register(KeteranganPrioritasNasional)
