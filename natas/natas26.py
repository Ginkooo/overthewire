from natas import Natas
import subprocess
import string
import random

PHPSESSID = 'asdf'

fn = ''.join([random.choice(string.ascii_letters) for _ in range(10)])
fn += '.php'

natas = Natas('natas26', keep_session=True)

drawing = subprocess.check_output('php natas26.php %s' % fn, shell=True).decode()

natas.set_cookie('drawing', drawing)

resp = natas.get_response()

resp = natas.get_response(relative_url='img/%s' % fn)

print(str(resp).strip())
