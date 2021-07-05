from import_export.admin import ImportExportActionModelAdmin
from .models import PythonTip


class PythonTipResource(ImportExportActionModelAdmin):
    class Meta:
        model = PythonTip
