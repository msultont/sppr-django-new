from django.contrib import admin
from .models import *


class FilesAdmin(admin.ModelAdmin):
    readonly_fields = ["uploaded_by", "uploaded_at"]

    def save_model(self, request, obj, form, change) -> None:
        obj.uploaded_by = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(File, FilesAdmin)
admin.site.register(FileHistory)

# Register your models here.
