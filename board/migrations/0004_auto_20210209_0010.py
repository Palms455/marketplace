# Generated by Django 3.1.5 on 2021-02-08 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20210208_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='sub_categories',
            field=models.ManyToManyField(blank=True, null=True, related_name='_category_sub_categories_+', to='board.Category', verbose_name='Подкатегории'),
        ),
    ]
