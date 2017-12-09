import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth


class Natas:

    def __init__(self, username: str, password: str='', keep_session: bool=False, quiet=False, custom_url=''):
        if not password:
            temp = self._get_pass_from_config(username)
            if temp:
                if not quiet:
                    print('Password loaded from passwords file')
                password = temp
            else:
                if not quiet:
                    print('Using empty password!')
        self.password = password
        self.username = username
        self.custom_url = custom_url
        if keep_session:
            self.session = self._create_session()
        else:
            self.session = None

    def _create_session(self):
        return requests.Session()

    def renew_session(self):
        self.session = self._create_session()

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

    def get_cookies(self):
        return self.session.cookies.get_dict()

    def set_cookie(self, key: str, value: str=None):
        self.session.cookies.set(key, value)

    def get_response(self, return_raw_response: bool=False, relative_url: str='', get_data: dict={}, post_data: dict={}, **kwargs) -> BeautifulSoup:
        if not post_data:
            post_data = kwargs.get('data', {})
        kwargs['data'] = post_data
        get = ''
        for k, v in get_data.items():
            get += '{}={}&'.format(k, v)

        if get:
            get = '?' + get[:-1]

        if not self.custom_url:
            url = 'http://{}.natas.labs.overthewire.org{}/{}'.format(self.username,
                                                                 get, relative_url)
        else:
            url = self.custom_url + get

        auth = HTTPBasicAuth(self.username, self.password)

        if self.session:
            response = self.session.post(url, auth=auth, **kwargs)
        else:
            response = requests.post(url, auth=auth, **kwargs)

        if return_raw_response:
            return response

        bs4 = BeautifulSoup(response.content, 'html.parser')

        return bs4
