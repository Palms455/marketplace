from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from board.models import Category, Tags, SaleProduct
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer, SaleProductSerializer, ListSaleProductSerializer


class CategoryApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        category = request.query_params.get("category")
        print(category)
        if not category:
            obj = Category.objects.filter(parent_categories__isnull=True)
        else:
            obj = Category.objects.filter(parent_categories__slug=category)
        serializers = CategorySerializer(obj, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class ListProductAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        obj = SaleProduct.objects.all()
        serializer = ListSaleProductSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SaleProductApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        obj = SaleProduct.objects.all()
        serializer = SaleProductSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

