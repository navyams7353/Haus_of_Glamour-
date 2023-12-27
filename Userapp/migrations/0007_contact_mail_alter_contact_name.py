# Generated by Django 4.1.4 on 2023-12-21 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0006_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='mail',
            field=models.EmailField(default='null@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Name',
            field=models.CharField(max_length=30),
        ),
    ]