from natas import Natas

natas = Natas('natas20', keep_session=True)

post = {
        'name': 'siema\nadmin 1',
        'password': 'dupa'
        }

get = {
        'debug': 'true'
        }

for i in range(2):
    r = natas.get_response(post_data=post, get_data=get)
    print(r.text)
