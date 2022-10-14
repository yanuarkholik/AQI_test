from django.db import models

class Book(models.Model):
    judul = models.CharField(max_length=200)
    desc = models.TextField()
    cat = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200)
    price = models.PositiveBigIntegerField()
    stock = models.PositiveBigIntegerField()
    publisher = models.CharField(max_length=200)
