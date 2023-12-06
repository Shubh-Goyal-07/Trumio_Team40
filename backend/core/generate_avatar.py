import base64
import os
import requests
from PIL import Image
from io import BytesIO
from .models import AvatarURL
from .serializer import AvatarURLSerializer
from django.core.files import File
from django.core.files.base import ContentFile

def preprocess_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.resize((1024,1024))
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    return img_byte_arr

def generate_image(user_id, image_url):
    engine_id = "stable-diffusion-xl-1024-v1-0"
    api_host = os.getenv("API_HOST", "https://api.stability.ai")
    api_key = os.getenv("STABILITY_API_KEY")
    # img=preprocess_image("https://www.varchas23.in/assets/khetan-bcf44cef.png")
    img = preprocess_image(image_url)

    if api_key is None:
        raise Exception("Missing Stability API key.")

    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/image-to-image",
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        files={
            "init_image": img
        },
        data={
            "image_strength": 0.35,
            "init_image_mode": "IMAGE_STRENGTH",
            "text_prompts[0][text]": "A classy english ai 8k, 3D animated style. Dark gray background.",
            "cfg_scale": 7,
            "samples": 1,
            "steps": 30,
        }
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    for i, image in enumerate(data["artifacts"]):
        avatar_url = os.path.join("media", "avatar", image_url.split("/media/image/")[1])

        avatar_url_instance = AvatarURL(user_id=user_id, image_url=os.path.join("avatar", image_url.split("/media/image/")[1]))
        avatar_url_instance.save()

        # Save the image to media/avatar folder
        with open(avatar_url, "wb") as f:
            f.write(base64.b64decode(image["base64"]))

        

