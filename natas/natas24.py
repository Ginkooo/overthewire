from natas import Natas

natas = Natas('natas24', keep_session=True)

post = {
        'passwd[0]': 'asdf'
        }

r = natas.get_response(post_data=post)

print(r.text)
