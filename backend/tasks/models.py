from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=50, unique=True)
    desciption = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
