# Generated by Django 4.1.4 on 2023-11-30 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Service_Name', models.CharField(max_length=20)),
                ('Images', models.ImageField(default='null.jpg', upload_to='img')),
                ('Category', models.CharField(max_length=20)),
                ('Price', models.CharField(max_length=20)),
            ],
        ),
    ]
