# Generated by Django 4.0 on 2022-06-14 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0002_rename_food_image_foodimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='resto',
            name='closing_time',
            field=models.TimeField(default='00:00'),
        ),
        migrations.AddField(
            model_name='resto',
            name='opening_time',
            field=models.TimeField(default='06:00'),
        ),
    ]