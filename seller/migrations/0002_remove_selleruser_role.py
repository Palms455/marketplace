# Generated by Django 3.1.5 on 2021-01-31 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selleruser',
            name='role',
        ),
    ]