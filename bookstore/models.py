from django.db import models

# Create your models here.

class Book(models.Model):
    name=models.CharField('书名',max_length=20,default='')
    price=models.DecimalField('价格',max_digits=7,decimal_places=2)
    id=models.IntegerField('id',default=0,primary_key=True)
    is_active=models.BooleanField('是否活跃',default=True)
    class Meta:
        verbose_name='图书'
        verbose_name_plural=verbose_name
    def __str__(self):
        return '%s|%s'%(self.name,self.price)
