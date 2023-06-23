from django.contrib import admin
from .models import TestModel

@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['title']
    search_fields = ['title', 'description']
    fields = ['title', 'description', 'image']



