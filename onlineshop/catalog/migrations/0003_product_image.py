# Generated by Django 3.2.7 on 2021-09-15 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20210914_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='static/img', verbose_name='Изображение'),
        ),
    ]
