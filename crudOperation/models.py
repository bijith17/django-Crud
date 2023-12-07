from django.db import models

class CrudOperation(models.Model):
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)