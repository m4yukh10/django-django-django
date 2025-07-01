from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=150)
    heading = models.TextField(max_length=750)
    content = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)

    
