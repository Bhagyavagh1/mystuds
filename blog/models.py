from django.db import models
from django.contrib.auth.models import User #to access user class from admin module

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content=models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #return self.title
       return f'{self.title} created on {self.created}'