from django.db import models

# Create your models here.


class api_detail(models.Model):
    API = models.TextField()
    link = models.URLField()
    Description = models.TextField()
    Auth : models.CharField(max_length=3)
    HTTPs = models.CharField(max_length=3)
    CORS = models.CharField(max_length=3)
    Category = models.CharField(max_length=100)

