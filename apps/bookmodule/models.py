from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=255)