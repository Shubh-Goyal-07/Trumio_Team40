# yourapp/models.py

from django.db import models

def upload_to(instance, filename):
    return f'uploads/{instance.folder_name}/{filename}'

class UploadedFile(models.Model):
    folder_name = models.CharField(max_length=255)
    file = models.FileField(upload_to=upload_to)


class ProjectSession(models.Model):
    project_id = models.CharField(max_length=255)
    session_id = models.CharField(max_length=255)

class ChatSession(models.Model):
    session_id = models.CharField(max_length=255)
    question = models.CharField(max_length=255)