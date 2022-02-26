from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField('姓名',max_length=11)
class Book(models.Model):
    name=models.CharField('书名',max_length=11)
    authors=models.ManyToManyField(Author)