# Generated by Django 3.1.5 on 2021-01-29 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boarditem',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tag_items', to='board.Tags', verbose_name='Теги'),
        ),
    ]
