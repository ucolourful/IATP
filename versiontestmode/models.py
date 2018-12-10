from django.db import models


class VersionTestMode(models.Model):
    Version = models.ForeignKey("version.Version", on_delete=models.CASCADE, null=True)
    TestMode = models.ForeignKey("testmode.TestMode", on_delete=models.CASCADE, null=True)
    versiontmname = models.CharField("版本测试模式名称", max_length=64)

    class Meta:
        verbose_name = "版本测试模式管理"
        verbose_name_plural = "版本测试模式管理"

    def __str__(self):
        return self.versiontmname
