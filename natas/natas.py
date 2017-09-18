import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth


class Natas:

    def __init__(self, username: str, password: str=''):
        if not password:
            temp = self._get_pass_from_config(username)
            if temp:
                print('Password loaded from passwords file')
                password = temp
            else:
                print('Using empty password!')
        self.password = password
        self.username = username

    def _get_pass_from_config(self, username: str):
        with open('passwords') as f:
            for line in f:
                line = line.strip()
                try:
                    user, password = line.split(' ')
                except ValueError:
                    continue
                if user == username:
                    return password
            return None

    def get_response(self, relative_url: str='', get_data: dict={}, post_data: dict={}, **kwargs) -> BeautifulSoup:
        if not post_data:
            post_data = kwargs.get('data', {})
        kwargs['data'] = post_data
        get = ''
        for k, v in get_data.items():
            get += '{}={}&'.format(k, v)

        if get:
            get = '?' + get[:-1]

        url = 'http://{}.natas.labs.overthewire.org{}/{}'.format(self.username,
                                                              get, relative_url)

        auth = HTTPBasicAuth(self.username, self.password)

        response = requests.post(url, auth=auth, **kwargs)

        bs4 = BeautifulSoup(response.content, 'html.parser')

        return bs4
