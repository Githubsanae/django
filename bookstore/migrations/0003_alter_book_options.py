# Generated by Django 3.2.5 on 2022-02-26 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_auto_20220225_1131'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '图书', 'verbose_name_plural': '图书'},
        ),
    ]
