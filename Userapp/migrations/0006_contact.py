# Generated by Django 4.1.4 on 2023-12-19 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0005_book_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.CharField(max_length=30)),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Userapp.register')),
            ],
        ),
    ]
