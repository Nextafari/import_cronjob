from django.urls import path

from . import views

urlpatterns = [
    path('python_tips', views.GetPythonTipsView.as_view(), name="python_tips"),
    path('create_tip', views.CreatePythonTipView.as_view(), name="create_tip"),
    path('edit_tip/<int:id>', views.EditTipView.as_view(), name="edit_tip"),
    path(
        'delete_tip/<int:id>',
        views.DeletePythonTipView.as_view(),
        name="delete_tip"
    ),
    path(
        'rest-auth/twitter/',
        views.TwitterLogin.as_view(), name='twitter_login'
    ),
]
