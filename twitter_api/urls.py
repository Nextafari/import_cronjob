from django.urls import path
from . import views

urlpatterns = [
    path('python_tips', views.GetPythonTipsView.as_view(), name="testing"),
    path('create_tip', views.CreateAPIView.as_view(), name="testing"),
    path('edit_tip/<int:id>', views.CreateAPIView.as_view(), name="testing"),
]
