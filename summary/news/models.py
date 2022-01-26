from django.db import models


# Create your models here.
class Summary(models.Model):
    objects = models.Manager()
    text = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True)
