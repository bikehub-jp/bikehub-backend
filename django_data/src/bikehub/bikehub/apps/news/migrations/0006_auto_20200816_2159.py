# Generated by Django 3.0 on 2020-08-16 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20200809_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='summary',
            field=models.TextField(blank=True, default=''),
        ),
    ]
