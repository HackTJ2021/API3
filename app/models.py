from django.db import models


class MyFile(models.Model):
    file = models.ImageField()
