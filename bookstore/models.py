from django.db import models

# Create your models here.

class Book(models.Model):
    name=models.CharField('书名',max_length=20,default='')
    price=models.DecimalField('价格',max_digits=7,decimal_places=2)

    def __str__(self):
        return '%s|%s'%(self.name,self.price)
