# Generated by Django 4.2.4 on 2023-09-09 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_adverts', '0006_alter_advertisement_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='photo',
            new_name='image',
        ),
    ]