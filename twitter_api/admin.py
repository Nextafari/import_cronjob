from django.contrib import admin
# from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from .models import PythonTip


class PythonTipResource(ImportExportActionModelAdmin):
    class Meta:
        model = PythonTip
    list_display = [
        "timestamp", "python_tip", "link",
        "author", "published"
    ]


admin.site.register(PythonTip, PythonTipResource)
