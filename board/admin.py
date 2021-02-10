from django.contrib import admin
from .models import Category, Tags, SaleProduct, ProductImages
from django_json_widget.widgets import JSONEditorWidget
from django.contrib.postgres import fields
from django.db import models
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category



class ImageAdmin(admin.TabularInline):
    model = ProductImages
    extra = 0


@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    model = Tags


@admin.register(SaleProduct)
class BoardAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }
    filter_horizontal = ('tags',)

    inlines = [ImageAdmin]
