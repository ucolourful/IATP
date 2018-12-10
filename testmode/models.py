from django.db import models


class TestMode(models.Model):
    testmodename = models.CharField('测试模式名称', max_length=64)
    testmodedesc = models.CharField('测试模式描述', max_length=200)
    create_time = models.DateTimeField('创建时间', auto_now=True)

    class Meta:
        verbose_name = "测试模式管理"
        verbose_name_plural = "测试模式管理"

    def __str__(self):
        return self.testmodename
