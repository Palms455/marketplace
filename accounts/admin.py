from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
# Register your models here.

from .models import Role, Account


# class RoleAdmin(admin.TabularInline):
#     model = Role
#     extra = 0


@admin.register(Account)
class UseAdmin(UserAdmin):
    model = Account
    #inlines = [RoleAdmin]

