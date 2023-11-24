from django.db import models
from django.core.validators import FileExtensionValidator
from django.db import models


class Pointers(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100)
    pointer = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    def __str__(self):
        return self.pointer

class AudioURL(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    audio_url = models.FileField(upload_to='audio/', validators=[FileExtensionValidator(allowed_extensions=['mp3'])])
    def __str__(self):
        return self.audio_url
