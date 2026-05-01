from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)
    quantity = models.IntegerField(default=0)
    pubdate = models.DateField()
    rating = models.FloatField(default=0.0)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    authors = models.ManyToManyField('Author')

class Publisher(models.Model):
    name = models.CharField(max_length=100)
location = models.CharField(max_length=300, null=True, blank=True)
class Author(models.Model):
    name = models.CharField(max_length=100)
    DOB = models.DateField()

class Address(models.Model):
    city = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    