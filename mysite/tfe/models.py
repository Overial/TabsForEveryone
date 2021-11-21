from django.db import models
from django.contrib.auth.models import User


class Tab(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    band = models.CharField(max_length=100)
    album = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    tab_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.band + ' – ' + self.title
