from rest_framework import serializers
from board.models import Category, SaleProduct, ProductImages, Tags
from accounts.models import Account

class AccountSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source="role.name")

    class Meta:
        model = Account
        fields = ("first_name", "last_name", "middle_name", "role", "phone")


class CategorySerializer(serializers.ModelSerializer):
    parent_categories = serializers.SlugField(source="parent_categories.slug")

    class Meta:
        model = Category
        fields = "__all__"


class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = "__all__"


class ProductImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImages
        fields = "__all__"


class ListSaleProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagsSerializer(many=True)
    images = ProductImagesSerializer(many=True)
    class Meta:
        model = SaleProduct
        fields = ("id", "title", "current_price", "old_price", "category", "tags", "publish_date", "images")


class SaleProductSerializer(serializers.ModelSerializer):
    author = AccountSerializer(read_only=True)
    category = CategorySerializer()
    tags = TagsSerializer(many=True)
    images = ProductImagesSerializer(many=True)

    class Meta:
        model = SaleProduct
        fields = "__all__"

