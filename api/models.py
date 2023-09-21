from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title= models.CharField(max_length=58)
    description= models.TextField(max_length=150)
    status= models.BooleanField(default=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def __str__(self) :
        return str(self.title)

