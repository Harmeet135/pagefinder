# Generated by Django 4.2.2 on 2023-06-26 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_alter_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='image_color',
            field=models.FileField(blank=True, max_length=250, null=True, upload_to='images/'),
        ),
    ]
