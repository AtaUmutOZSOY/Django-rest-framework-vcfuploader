from django.contrib import admin

# Register your models here.

from uploader.models import VcfFile

admin.site.register(VcfFile)