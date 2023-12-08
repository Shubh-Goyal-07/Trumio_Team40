from django.db import models
from django.core.validators import FileExtensionValidator
from django.db import models


class Pointers(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100)
    pointers = models.TextField()
    topic = models.CharField(max_length=100)
    def __str__(self):
        return self.pointer

class AudioURL(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    audio_url = models.FileField(upload_to='audio/', validators=[FileExtensionValidator(allowed_extensions=['mp3'])])
    def __str__(self):
        return self.user_id

class ImageURL(models.Model):
    user_id = models.CharField(max_length=100)
    image_url = models.FileField(upload_to='image/', validators=[FileExtensionValidator(allowed_extensions=['jpg','png','jpeg'])])
    def __str__(self):
        return self.user_id
    
class AvatarURL(models.Model):
    user_id = models.CharField(max_length=100)
    image_url = models.FileField(upload_to='avatar/', validators=[FileExtensionValidator(allowed_extensions=['jpg','png','jpeg'])])
    def __str__(self):
        return self.image_url
    
class AvatarURL(models.Model):
    user_id = models.CharField(max_length=100)
    image_url = models.FileField(upload_to='avatar/', validators=[FileExtensionValidator(allowed_extensions=['jpg','png','jpeg'])])
    def __str__(self):
        return self.image_url

class CreateVideo(models.Model):
    image_url = models.CharField(max_length=100)
    content = models.TextField()
    user_id = models.CharField(max_length=100)
    unique_id = models.CharField(max_length=100)
    def __str__(self):
        return self.image_url


class Timeline(models.Model):
    project_id = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    weeks = models.CharField(max_length=100)
    timeline = models.TextField()
    def __str__(self):
        return self.project_id
    
