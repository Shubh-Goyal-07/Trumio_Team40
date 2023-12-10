import base64
import os
import requests
from PIL import Image
from io import BytesIO
from .models import AvatarURL
import time
from .serializer import AvatarURLSerializer
from django.core.files import File
from django.core.files.base import ContentFile
import environ
env = environ.Env()
environ.Env.read_env()
import json

def preprocess_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.resize((1024,1024))
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    return img_byte_arr

def generate_avatar(image_url):
    print("imageurl is ",image_url)
    posturl = "https://api.thenextleg.io/ppu/imagine"

    
    payload = json.dumps({
    "msg": f"{image_url} full body, realistic detailed 3d avatar with nice human facial features, life like expression, realistic skin tone, facial details and expressions, light condition for accurate representation",
    "ref": "",
    "webhookOverride": "", 
    "ignorePrefilter": "false"
    })

    headers = {
    'Authorization': 'Bearer '+os.environ['NEXT_LEG_API_KEY'],
    'Content-Type': 'application/json'
    }

    response_post = requests.request("POST", posturl, headers=headers, data=payload)
    response_post = response_post.json()
    return response_post
        





        

