from django.db import models
from .helpers import get_upload_dir


class Category(models.Model):
    """Категория"""
    name = models.CharField(max_length=150, verbose_name="Категория")
    description = models.CharField(max_length=500, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        db_table = '"catalog"."category"'
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Subcategory(models.Model):
    """Подкатегория"""
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Основная категория", related_name="subcategories")

    def __str__(self):
        return self.name

    class Meta:
        db_table = '"catalog"."subcategory"'
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


class Tags(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название тега")

    class Meta:
        db_table = '"catalog"."tags"'
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class BoardItem(models.Model):
    """Объявление"""
    title = models.CharField(max_length=150, null=False, blank=False, verbose_name="Название")
    description = models.TextField(null=False, blank=False, verbose_name="Описание")
    current_price = models.DecimalField(decimal_places=2, null=True, blank=True, verbose_name="Текущая цена")
    old_price = models.DecimalField(decimal_places=2, null=True, blank=True, verbose_name="Прошлая цена")
    subcategories = models.ForeignKey(Subcategory, on_delete=models.PROTECT, verbose_name="Подкатегории", related_name="subcategories")
    tags = models.ManyToManyField(Tags, verbose_name="Теги")

    class Meta:
        db_table = '"catalog"."board_item"'
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.title


class BoardImages(models.Model):
    """Изображения"""
    image = models.ImageField(upload_to=get_upload_dir)
    board_item = models.ForeignKey(BoardItem, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Изображения")

    class Meta:
        db_table = '"catalog"."board_images"'
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товаров"