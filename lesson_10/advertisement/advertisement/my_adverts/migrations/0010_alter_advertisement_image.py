# Generated by Django 4.2.4 on 2023-09-18 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_adverts', '0009_remove_advertisement_ababa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(blank=True, upload_to='my_adverts', verbose_name='Изображение'),
        ),
    ]
