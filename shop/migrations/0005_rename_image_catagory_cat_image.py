# Generated by Django 4.2 on 2023-04-19 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_favourite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catagory',
            old_name='image',
            new_name='cat_image',
        ),
    ]