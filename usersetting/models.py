from django.db import models


class UserSetting(models.Model):
    username = models.CharField('用户名', max_length=150)
    product_id = models.IntegerField('产品线id', null=True)
    product_name = models.CharField('产品线名称', max_length=64, null=True)
    version_id = models.IntegerField('版本id', null=True)
    version_name = models.CharField('版本名称', max_length=64, null=True)

    class Meta:
        verbose_name = '用户自定义设置'
        verbose_name_plural = '用户自定义设置'

    def __str__(self):
        return self.username
