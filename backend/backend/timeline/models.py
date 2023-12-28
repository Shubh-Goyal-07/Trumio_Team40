from django.db import models

# Create your models here.

class Timeline(models.Model):
    project_id = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    weeks = models.CharField(max_length=100)
    timeline = models.TextField()
    def __str__(self):
        return self.project_id