# Generated by Django 3.0.5 on 2021-11-09 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_auto_20211109_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_name',
            field=models.CharField(max_length=100),
        ),
    ]