from django.contrib import admin
from devices.models import *
# Register your models here.


class DispositivoAdminInLine(admin.TabularInline):
    model = Device
    extra = 1

@admin.register(Environment)
class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'update']

    inlines = [DispositivoAdminInLine]