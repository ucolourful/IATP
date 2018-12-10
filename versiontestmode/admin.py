from django.contrib import admin

from versiontestmode.models import VersionTestMode


class VersionTestModeAdmin(admin.ModelAdmin):
    list_display = ['Version', 'TestMode', 'versiontmname']
    list_filter = ['Version', 'TestMode']


admin.site.register(VersionTestMode, VersionTestModeAdmin)
