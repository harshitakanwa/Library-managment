# Generated by Django 3.0.5 on 2021-11-03 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='request_status',
            field=models.BooleanField(default=False),
        ),
    ]
