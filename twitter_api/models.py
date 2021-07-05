from django.db import models


class PythonTip(models.Model):
    class Meta:
        verbose_name = "Python Tip"
        verbose_name_plural = "Python Tips"
    timestamp = models.CharField(max_length=25)
    python_tip = models.CharField(max_length=140)
    link = models.URLField()
    author = models.CharField(max_length=25)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.python_tip

