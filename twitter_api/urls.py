from django.urls import path
from . import views

urlpatterns = [
    path('new_data', views.TestViee.as_view(), name="testing")
]