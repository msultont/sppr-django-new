from django.contrib import admin
from .models import CsvLongList, Longlist, ShortList

# Register your models here.

admin.site.register(Longlist)
admin.site.register(ShortList)
admin.site.register(CsvLongList)
