from django.db import models


class PythonTipSheet(models.Model):
    class Meta:
        verbose_name = "Python Tip Sheet"
        verbose_name_plural = "Python Tips Sheet"
    timestamp = models.CharField(max_length=25)
    python_tip = models.CharField(max_length=140)
    link = models.URLField()
    author = models.CharField(max_length=25)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.python_tip


class PythonTipUserForm(models.Model):
    class Meta:
        verbose_name = "Python Tip User Form"
        verbose_name_plural = "Python Tips User Forms"
    python_tip = models.CharField(max_length=140)
    twitter_handle = models.CharField(max_length=20)
    email = models.CharField(max_length=40)

    def __str___(self):
        return self.email
