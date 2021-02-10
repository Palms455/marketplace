# Generated by Django 3.1.5 on 2021-02-10 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0005_auto_20210210_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleproduct',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.account', verbose_name='Продавец'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tags',
            name='slug',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Символьный код'),
        ),
    ]