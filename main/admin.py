from django.contrib import admin
from .models import TestItem
# Register your models here.


@admin.register(TestItem)
class TestItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'site']
