# Generated by Django 3.0.5 on 2021-11-09 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_auto_20211108_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='subscription_type',
            field=models.CharField(choices=[('Basic', 'Basic'), ('Prime', 'Prime')], default=0, max_length=30),
        ),
    ]
