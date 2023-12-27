from django.db import models

# Create your models here.
class Category(models.Model):
    Cat_Name=models.CharField(max_length=20)
    Image=models.ImageField(upload_to='images' ,default='null.jpg')
    Description=models.CharField(max_length=20)
class Service(models.Model):
    Service_Name=models.CharField(max_length=20)
    Images=models.ImageField(upload_to='img' ,default='null.jpg')
    category=models.CharField(max_length=20)
    Price=models.CharField(max_length=20)
class Branch(models.Model):
    Branch_Name=models.CharField(max_length=20)
    Img=models.ImageField(upload_to='image' ,default='null.jpg')
    Location=models.CharField(max_length=20)
