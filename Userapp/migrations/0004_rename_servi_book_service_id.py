# Generated by Django 4.1.4 on 2023-12-13 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0003_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Servi',
            new_name='Service_id',
        ),
    ]
