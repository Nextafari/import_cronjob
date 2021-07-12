# from django.contrib.admin.options import BaseModelAdmin
from django.db import models


class PythonTipSheet(models.Model):
    timestamp = models.CharField(max_length=25, blank=True, null=True)
    python_tip = models.CharField(max_length=140, blank=True, null=True)
    link = models.CharField(max_length=140, blank=True, null=True)
    author = models.CharField(max_length=25, blank=True, null=True)
    published = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Python Tip Sheet"
        verbose_name_plural = "Python Tips Sheet"

    def __str__(self):
        return self.python_tip


class PythonTipUserForm(models.Model):
    python_tip = models.CharField(max_length=140, blank=True, null=True)
    twitter_handle = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        verbose_name = "Python Tip User Form"
        verbose_name_plural = "Python Tips User Forms"

    def __str___(self):
        return self.email
