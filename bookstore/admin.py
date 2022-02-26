from django.contrib import admin
from .models import Book
# Register your models here.

class BookManager(admin.ModelAdmin):
    list_display = ['id','name','price','is_active']
    list_display_links = ['name']
    list_filter = ['price']
    search_fields = ['name']
    list_editable = ['price']
admin.site.register(Book,BookManager)
