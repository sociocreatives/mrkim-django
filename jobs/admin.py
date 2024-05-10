from django.contrib import admin
from .models import Category
from .models import MajorCategory
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Category, ImportExportModelAdmin)
admin.site.register(MajorCategory, ImportExportModelAdmin)