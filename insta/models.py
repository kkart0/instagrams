from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Profiles(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=100,default="")
    email=models.EmailField(max_length=100,default="")
    mobile=models.CharField(max_length=10,default="")
    age=models.CharField(max_length=4,default="")
    gender=models.CharField(max_length=10,default="")
    Passward=models.CharField(max_length=100,default="")
   
    def __str__(self):
        return self.name
class Post(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=100,default="")
    image=models.ImageField(default="")
    def __str__(self):
        return self.name
class Cuser(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=100,default="")
    def __str__(self):
        return self.name