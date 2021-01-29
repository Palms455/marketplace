from django.contrib import admin
from .models import Category, Subcategory, Tags, BoardItem, BoardImages
# Register your models here.

class SubcategoryAdmin(admin.TabularInline):
    model = Subcategory
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    inlines = [SubcategoryAdmin]


class ImageAdmin(admin.TabularInline):
    model = BoardImages
    extra = 0


@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    model = Tags


@admin.register(BoardItem)
class BoardAdmin(admin.ModelAdmin):
    model = BoardItem
    filter_horizontal = ('tags',)

    inlines = [ImageAdmin]
