# Generated by Django 3.1.5 on 2021-02-08 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Символьный код'),
        ),
        migrations.AddField(
            model_name='category',
            name='sub_categories',
            field=models.ManyToManyField(related_name='_category_sub_categories_+', to='board.Category', verbose_name='Подкатегории'),
        ),
    ]