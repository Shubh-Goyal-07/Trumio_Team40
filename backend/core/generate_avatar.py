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
    if(response_post['success']==False):
        print(response_post, "in error block")
        raise Exception("Something went wrong with the Avatar API")
    
    print(response_post)
    ppuId = response_post.json()['messageId']

    geturl=f"https://api.thenextleg.io/ppu/message/<messageId>?ppuId={ppuId}"

    headers = {
        'Authorization': 'Bearer '+os.environ['NEXT_LEG_API_KEY'],
    }

    response_get = requests.request("GET", geturl, headers=headers)

    while(response_get.json()['progress']!=100):
        time.sleep(5)
        response_get = requests.request("GET", geturl, headers=headers)
    
    
    return response_get.json()
        





        

