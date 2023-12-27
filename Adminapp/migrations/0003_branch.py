# Generated by Django 4.1.4 on 2023-12-01 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0002_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Branch_Name', models.CharField(max_length=20)),
                ('Image', models.ImageField(default='null.jpg', upload_to='image')),
                ('Services', models.CharField(max_length=20)),
            ],
        ),
    ]
