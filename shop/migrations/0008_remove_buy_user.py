# Generated by Django 4.2 on 2023-04-20 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_buy_mobilenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buy',
            name='user',
        ),
    ]
