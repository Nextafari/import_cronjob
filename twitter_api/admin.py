from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from .models import PythonTipSheet, PythonTipUserForm


# tip_resource = PythonTipSheetResource()
# dataset = tip_resource.export()
# dataset.xlsx
class PythonTipResource(resources.ModelResource):

    class Meta:
        model = PythonTipSheet
        fields = (
            "timestamp", "python_tip", "link",
            "author", "published",
        )


class PythonTipSheetAdmin(ImportExportActionModelAdmin):
    class Meta:
        model = PythonTipSheet
    list_display = [
        "timestamp", "python_tip", "link",
        "author", "published"
    ]


admin.site.register(PythonTipSheet, PythonTipSheetAdmin)


class PythonTipFormAdmin(admin.ModelAdmin):
    list_display = [
        "python_tip", "twitter_handle", "email"
    ]


admin.site.register(PythonTipUserForm, PythonTipFormAdmin)
