from django.db import models
# models.py

# models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # ทำการเพิ่มฟิลด์เพิ่มเติมตามต้องการ
    birth_date = models.DateField(null=True, blank=True)
    
    # กำหนด related_name ให้กับ groups และ user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )



# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name+","+str(self.age)