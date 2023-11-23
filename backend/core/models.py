from django.db import models

# Create your models here.

class Pointers(models.Model):
    user_id = models.CharField(max_length=100)
    pointer = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    def __str__(self):
        return self.pointer
