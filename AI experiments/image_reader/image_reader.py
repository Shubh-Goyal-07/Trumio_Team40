# Authentication to Google API
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'vision_key.json'

from google.cloud import vision

# re is used to extract IMEI using regex
import re


vision_client = vision.ImageAnnotatorClient()
image = vision.Image()

image_uri = './test.png'

image.source.image_uri = image_uri


response = vision_client.text_detection(image=image)