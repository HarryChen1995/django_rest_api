from django.db import models
# Create your models here.
from datetime import datetime

class Message(models.Model):
        is_incomming = models.BooleanField(default=False)
        content = models.CharField(max_length=30)
        created = models.DateTimeField(auto_now=True)