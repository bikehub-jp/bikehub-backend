# Generated by Django 3.0.7 on 2020-09-05 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200905_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='ubike1_by_list',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='ubike2_by_list',
        ),
    ]