from django.db import models


class Version(models.Model):
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)
    versionname = models.CharField('版本名称', max_length=64)
    versiondesc = models.CharField('版本描述', max_length=200)
    versionperson = models.CharField('版本负责人', max_length=200)
    create_time = models.DateTimeField('创建时间', auto_now=True)

    class Meta:
        verbose_name = '版本管理'
        verbose_name_plural = '版本管理'

    def __str__(self):
        return self.versionname
