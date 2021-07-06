from django.contrib import admin
# from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from .models import PythonTipSheet, PythonTipUserForm


class PythonTipResource(ImportExportActionModelAdmin):
    class Meta:
        model = PythonTipSheet
    list_display = [
        "timestamp", "python_tip", "link",
        "author", "published"
    ]


admin.site.register(PythonTipSheet, PythonTipResource)


class PythonTipFormAdmin(admin.ModelAdmin):
    list_display = [
        "python_tip", "twitter_handle", "email"
    ]


admin.site.register(PythonTipUserForm, PythonTipFormAdmin)
