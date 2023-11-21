# yourapp/models.py

from django.db import models



class ProjectSession(models.Model):
    project_id = models.CharField(max_length=255)
    project_link = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)


class ChatSession(models.Model):
    project_id = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    question = models.CharField(max_length=255)