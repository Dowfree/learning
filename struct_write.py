import struct


n = 1300000
x = 96.45
b = True
s = 'hello world'
sn = struct.pack('if?', n, x, b)
f = open('sample_struct.dat', 'wb')
f.write(sn)
f.write(s.encode('utf-8'))
f.close()
