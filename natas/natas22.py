from natas import Natas

natas = Natas('natas22', keep_session=True)

get = {
        'revelio': 'asdf'
        }

resp = natas.get_response(get_data=get, return_raw_response=True, allow_redirects=False)

print(natas.get_cookies())
print(resp.text)
