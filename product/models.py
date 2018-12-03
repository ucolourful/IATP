from django.db import models


class Product(models.Model):
    productname = models.CharField('产品线名称', max_length=64)
    productdesc = models.CharField('产品线描述', max_length=200)
    producter = models.CharField('产品线负责人', max_length=200)
    create_time = models.DateTimeField('创建时间', auto_now=True)

    class Meta:
        verbose_name = '产品线管理'
        verbose_name_plural = '产品线管理'

    def __str__(self):
        return self.productname
