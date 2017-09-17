import base64
from itertools import cycle
xored_and_64 = b'ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSRwh6QUcIaAw='  # cookie

decoded = base64.decodebytes(xored_and_64)  # decoded cookie

text = b'{"showpassword":"no","bgcolor":"#ffffff"}'  # xored decoded cookie

ret = []

for i, l in zip(text, decoded):
    ret.append(hex(i ^ l))


def xor_encrypt(data):
    key = [int(x, 16) for x in ['0x71', '0x77', '0x38', '0x4a']]
    ret = []
    long_key = cycle(key)

    for i, l in zip(data, long_key):
        ret.append(hex(i ^ l))

    return ret


hexarr = xor_encrypt(xored_and_64)  # array decoded as hex array

x = ''.join(['0'+bin(int(x, 16))[2:] for x in hexarr])  # binary for that array


text = b'{"showpassword":"yes","bgcolor":"#ffffff"}'
xored = xor_encrypt(text)
xored_bytes = bytes([int(a, 16) for a in xored])

print(base64.encodebytes(xored_bytes))
