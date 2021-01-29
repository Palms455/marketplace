from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.core.validators import RegexValidator

class Role(models.Model):
    name = models.CharField(max_length=36, blank=False, null=False, unique=True, verbose_name="Наименование")


class SellerUser(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?7?\d{9,15}$',
                                 message="Телефонный номер должен иметь формат: '+7 999 999 9999'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    role = models.ForeignKey(Role, null=False, blank=False, on_delete=models.PROTECT, verbose_name="Роль")


class GroupProxy(Group):
    """Прокси-модель для групп пользователей"""

    class Meta:
        proxy = True
        verbose_name_plural = "Группы"
        verbose_name = "Группа"