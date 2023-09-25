from django.db import models
from django.contrib.auth.models import User

    
class Category(models.Model):
    name=models.CharField(max_length=100,default=None)

    def __str__(self) :
        return self.name

# Create your models here.
class Project(models.Model):
    Category= models.ForeignKey(Category,on_delete=models.CASCADE,related_name='projects',default=None)
    title= models.CharField(max_length=58)
    description= models.TextField(max_length=150)
    status= models.BooleanField(default=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def __str__(self) :
        return str(self.title)
    
    
class Collection(models.Model):
    title=models.CharField(max_length=50)
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='collection')
    description=models.TextField(blank=True,max_length=100)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def __str__(self) :
        return str(self.title)
    
class Environment(models.Model):
    fields = models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    project=models.ForeignKey(Project, on_delete=models.CASCADE,default=None,related_name='environment')
    
    def __str__(self) :
        return str(self.title)
    

