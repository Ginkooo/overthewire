from natas import Natas

natas = Natas('natas23', keep_session=True)

get = {
        'passwd': 
        }

r = natas.get_response(get_data=get)
print(r.text)
