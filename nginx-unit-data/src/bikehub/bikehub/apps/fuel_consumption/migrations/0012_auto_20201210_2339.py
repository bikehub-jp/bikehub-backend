# Generated by Django 3.0.7 on 2020-12-10 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuel_consumption', '0011_auto_20201209_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='maker_str',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AddField(
            model_name='eda',
            name='max_eda',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='eda',
            name='min_eda',
            field=models.IntegerField(default=0),
        ),
    ]