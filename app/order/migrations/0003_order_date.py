# Generated by Django 4.0 on 2022-06-17 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_amount_of_people'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
