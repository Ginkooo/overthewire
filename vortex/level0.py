#!/usr/bin/env python3

import ctypes
import socket

uint_size = ctypes.sizeof(ctypes.c_uint())

s = socket.socket()
s.connect(('vortex.labs.overthewire.org', 5842))

result = [s.recv(uint_size), s.recv(uint_size),
          s.recv(uint_size), s.recv(uint_size)]

sum_ = 0
for x in result:
    sum_ += int.from_bytes(x, byteorder='little')

s.sendall(sum_.to_bytes(uint_size, 'little'))
print(s.recv(4096))
