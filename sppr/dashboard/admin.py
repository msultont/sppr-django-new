from django.contrib import admin
from .models import AnalisisKerangkaLogis, CsvLongList, DataKawasanPrioritas, IsuStrategis, Longlist
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin

# Register your models here.

admin.site.register(Longlist)
admin.site.register(CsvLongList)
admin.site.register(DataKawasanPrioritas)

admin.site.register(
    AnalisisKerangkaLogis,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
)

admin.site.register(
    IsuStrategis,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
)
