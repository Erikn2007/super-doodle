# Generated by Django 4.2.4 on 2023-09-14 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_adverts', '0007_rename_photo_advertisement_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='ababa',
            field=models.CharField(default=6, max_length=255),
            preserve_default=False,
        ),
    ]
