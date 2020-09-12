from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

#Blog model contains information related to all blogs...
class Blog(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    title=models.CharField(max_length=100,help_text='title...')
    text=models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uname=models.CharField(max_length=50)
    def __str__(self):
        return self.uname

#Personal model contains information of all users profile_pic and bio's...
class Personal(models.Model):
    uname=models.CharField(max_length=50, unique=True)
    bio=models.CharField(max_length=100)
    pic=models.ImageField()
    def __str__(self):
        return self.uname
    
    
   