# Generated by Django 3.0.7 on 2021-01-27 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0026_auto_20210127_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='video_id',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
    ]