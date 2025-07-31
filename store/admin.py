from django.contrib import admin

# Register your models here.

from.models import Category,Book
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("name",)}
    list_display=("name",)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=("title","author","price","stock","category")
    list_filter=("category",)
    search_fields=("title","author")
