from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# contact model
class Contact(models.Model):
    Name=models.CharField(max_length=70)
    Email=models.EmailField(max_length=150)
    Message=models.TextField()


class Commoninformation(models.Model):
    title=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    content=models.TextField()
    image=models.ImageField(upload_to='myimage')
    date=models.DateField()
    class Meta:
        abstract=True

class Politics(Commoninformation):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Politics_blog')


class Business(Commoninformation):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Business_blog')
