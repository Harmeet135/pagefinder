# Generated by Django 4.2.2 on 2023-06-26 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_remove_image_image_image_image_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image_color',
            new_name='image',
        ),
    ]
