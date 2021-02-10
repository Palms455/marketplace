from django.db import models
from .helpers import get_upload_dir
from django.db.models import JSONField
from pytils.translit import slugify
from accounts.models import Account


class Category(models.Model):
    """Категория"""
    name = models.CharField(max_length=150, verbose_name="Категория")
    description = models.CharField(max_length=500, verbose_name="Описание")
    parent_categories = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, related_name='child_categories', verbose_name="Родительская категория")
    slug = models.CharField(max_length=255, default="", verbose_name="Символьный код", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = '"catalog"."category"'
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save()


class Tags(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название тега")
    slug = models.CharField(max_length=255, default="", verbose_name="Символьный код", blank=True)

    class Meta:
        db_table = '"catalog"."tags"'
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tags, self).save()


class SaleProduct(models.Model):
    """Объявление"""
    id = models.AutoField(primary_key=True, verbose_name="Номер объявления")
    title = models.CharField(max_length=150, null=False, blank=False, verbose_name="Название")
    description = models.TextField(null=False, blank=False, verbose_name="Описание")
    current_price = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True, verbose_name="Текущая цена")
    old_price = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True, verbose_name="Прошлая цена")
    category = models.ForeignKey(Category, verbose_name="Категории", related_name="offers", on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tags, blank=True, related_name='tag_items', verbose_name="Теги")
    create_date = models.DateTimeField(auto_now=True, verbose_name="Дата создания")
    publish_date = models.DateTimeField(null=True, blank=True, verbose_name="Дата публикации")
    update_date = models.DateTimeField(null=True, blank=True, verbose_name="Дата обновления")
    upper_date = models.DateTimeField(null=True, blank=True, verbose_name="Дата поднятия")
    published = models.BooleanField(default=False, verbose_name="Статус объявления")
    extra_data = models.JSONField(blank=True, null=True, verbose_name="Дополнительное описание")
    author = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name="Продавец")
    # todo: JsonSchemaValidate

    class Meta:
        db_table = '"catalog"."sale_product"'
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.title


class ProductImages(models.Model):
    """Изображения"""
    image = models.ImageField(upload_to=get_upload_dir)
    board_item = models.ForeignKey(SaleProduct, null=True, blank=True, on_delete=models.CASCADE, related_name="images", verbose_name="Изображения")

    class Meta:
        db_table = '"catalog"."product_images"'
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товаров"