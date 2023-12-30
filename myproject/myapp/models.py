from django.db import models

# Create your models here.
class User(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    Mobno=models.BigIntegerField(primary_key=True)
    password=models.CharField(max_length=20)
    Adhaar=models.BigIntegerField()
    token = models.CharField(max_length=100)
    user_category = models.CharField(max_length=30)
    def __str__(self):
        name=f"{self.Name}"
        return name

class SuperAdmin(models.Model):
    Username=models.CharField(max_length=30)
    Password=models.CharField(max_length=50)

class AdminUser(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.EmailField()
    Mobno=models.BigIntegerField(primary_key=True)
    password=models.CharField(max_length=20)
    token = models.CharField(max_length=100)
    USER_TYPES = (
        ('3d', '3D PRINTING'),
        ('aqua', 'AQUA CULTURE'),
        ('water', 'WATER BODY MANAGEMENT'),
    )
    user_category = models.CharField(max_length=20, choices=USER_TYPES,default=USER_TYPES)
    def __str__(self):
        name = f"{self.user_category}"
        return name
    
