from django.contrib import admin
from .models import Choice, Provinsi, Question
from .models import Proyek

# Register your models here.

admin.site.register(Proyek)
admin.site.register(Provinsi)
admin.site.register(Question)
admin.site.register(Choice)
