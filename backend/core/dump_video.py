import urllib.request



def dump_video(link,id):
    # link = "https://d-id-talks-prod.s3.us-west-2.amazonaws.com/google-oauth2%7C109298312937099039705/tlk_ODDPx_jH6tGt0xhgDaFpH/1700733631233.mp4?AWSAccessKeyId=AKIA5CUMPJBIK65W6FGA&Expires=1700820038&Signature=RS%2FrB1LPqAZPRXO0zkifhBvrCcw%3D&X-Amzn-Trace-Id=Root%3D1-655f22c6-15eabdec5f419aca777869e3%3BParent%3D2fb52484f61bffa2%3BSampled%3D1%3BLineage%3D6b931dd4%3A0"

    urllib.request.urlretrieve(link, 'media/video/'+str(id)+'.mp4') 
    return 

