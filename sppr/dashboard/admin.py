from django.contrib import admin
from .models import CsvLongList, Longlist

# Register your models here.

admin.site.register(Longlist)
admin.site.register(CsvLongList)
