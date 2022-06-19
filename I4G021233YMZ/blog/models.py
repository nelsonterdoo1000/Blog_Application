from cgitb import text
from django.db import models
from pkg_resources import get_supported_platform
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    created_date = models.DateTimeField('date created')
    Published_date = models.DateTimeField('date published')
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
	    return self.Title