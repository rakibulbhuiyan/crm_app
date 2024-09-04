from django.contrib import admin
from crm.models import Record
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class RecordAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'first_name', 'last_name', 'email', 'phone', 'city', 'state']


admin.site.register(Record, RecordAdmin)
