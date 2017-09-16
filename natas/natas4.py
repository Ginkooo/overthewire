import requests
from requests.auth import HTTPBasicAuth


r = requests.get('http://natas4.natas.labs.overthewire.org/', headers={'Referer': 'http://natas5.natas.labs.overthewire.org/', 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'},
                 auth=HTTPBasicAuth('natas4', 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'))
print(r.content)
