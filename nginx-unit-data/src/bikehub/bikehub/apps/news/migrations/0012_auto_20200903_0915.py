# Generated by Django 3.0.7 on 2020-09-03 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20200831_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='featured_image',
            field=models.URLField(max_length=500),
        ),
    ]
