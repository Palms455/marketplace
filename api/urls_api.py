from django.urls import path
from . import views_api

urlpatterns = [
    path("get_categories/", views_api.CategoryApiView.as_view()),
    path("get_products/", views_api.SaleProductApiView.as_view()),
    path("get_list_products/", views_api.ListProductAPI.as_view())


]