from django.contrib import admin

from testmode.models import TestMode


class TestmodeAdmin(admin.ModelAdmin):
    list_display = ['testmodename', 'testmodedesc']
    search_fields = ['testmodename']


admin.site.register(TestMode, TestmodeAdmin)
