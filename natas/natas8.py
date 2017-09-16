import base64
import binascii


secret = '3d3d516343746d4d6d6c315669563362'

string_bin = binascii.unhexlify(secret)

string_bin = string_bin[::-1]

print(base64.decodestring(string_bin))
