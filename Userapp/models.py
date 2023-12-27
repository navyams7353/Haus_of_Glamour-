from django.db import models
from Adminapp.models import*
# Create your models here.
class Register(models.Model):
    User_Name=models.CharField(max_length=20)
    Pass_word=models.CharField(max_length=4)
    Phone_Number=models.CharField(max_length=10)
    Email=models.EmailField(default='null@gmail.com')
    Address=models.CharField(max_length=20)
class Book(models.Model):
    User_id=models.ForeignKey(Register, on_delete=models.CASCADE)
    Service_id=models.ForeignKey(Service, on_delete=models.CASCADE)
    Date=models.DateField(null=True)
    Time=models.TimeField()
    Status=models.IntegerField(default=0)
class Contact(models.Model):
    Name=models.CharField(max_length=30)
    mail=models.EmailField(default='null@gmail.com')
    Message=models.CharField(max_length=30)
