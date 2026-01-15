from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'fund_number', 'category', 'creation_date')
    search_fields = ('title', 'fund_number')