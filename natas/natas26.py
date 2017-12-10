from natas import Natas
from shutil import copyfileobj
import base64
import requests

IMAGEPATH = 'natas26image.png'

natas = Natas('natas26', keep_session=True)


def update_image(get_data):
    r = natas.get_response(get_data=get_data)
    img = r.find('img')
    src = img['src']
    src = natas.base_url + '/' + src
    r = requests.get(src, auth=natas.auth, stream=True)
    with open(IMAGEPATH, 'wb') as f:
        copyfileobj(r.raw, f)


get = {
        'x1': 5,
        'x2': 10,
        'y1': 2,
        'y2': 4
        }

update_image(get)
b = natas.get_cookies()['drawing'].encode('ascii')
b = b.replace(b'%3D', b'=')
b = base64.decodebytes(b)
print(b)

