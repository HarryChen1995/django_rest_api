from djongo import models
# Create your models here.
from datetime import datetime

class Comment(models.Model):
        email = models.EmailField(max_length = 30)
        content = models.CharField(max_length=30)
        created = models.DateTimeField(auto_now=True)