# Generated by Django 4.0 on 2022-06-07 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='infouser',
            name='phone_number',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
