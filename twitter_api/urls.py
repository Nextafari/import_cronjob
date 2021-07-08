from django.urls import path

from . import views

urlpatterns = [
    path('python_tips', views.GetPythonTipsView.as_view(), name="testing"),
    path('create_tip', views.CreatePythonTipView.as_view(), name="testing"),
    path('edit_tip/<int:id>', views.EditTipView.as_view(), name="testing"),
    path(
        'delete_tip/<int:id>',
        views.DeletePythonTipView.as_view(),
        name="testing"
    ),
]
