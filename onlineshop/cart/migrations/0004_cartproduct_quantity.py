# Generated by Django 3.2.7 on 2021-10-22 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_cartproduct_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproduct',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]