# Generated by Django 4.2.4 on 2023-09-09 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_adverts', '0004_advertisement_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='photo',
            field=models.ImageField(default=6, upload_to='', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
