# Generated by Django 3.1.5 on 2021-02-10 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20210209_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='sub_categories',
        ),
        migrations.AddField(
            model_name='category',
            name='parent_categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child_categories', to='board.category', verbose_name='Родительская категория'),
        ),
    ]
