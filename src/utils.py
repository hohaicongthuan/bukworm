import base64

def img_to_base64(img):
    return base64.b64encode(img).decode('ascii')