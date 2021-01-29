from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
# Register your models here.

from .models import Role, SellerUser


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    model = Role


@admin.register(SellerUser)
class UseAdmin(UserAdmin):
    model = SellerUser

