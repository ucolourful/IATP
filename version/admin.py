from django.contrib import admin

from version.models import Version


class VersionAdmin(admin.ModelAdmin):
    list_display = ['versionname', 'Product', 'versiondesc', 'versionperson', 'create_time', 'id']
    list_filter = ['Product', 'versionperson']
    search_fields = ['versionname', 'versionperson']
    # inlines = [ApisAdmin]


admin.site.register(Version, VersionAdmin)
