#!usr/bin/env python
# -*-coding:utf-8 -*-

import struct
filename = input('Please input the filename:')
with open(filename, 'rb') as fp:
    s = fp.read(30)
    key = struct.unpack('<ccIIIIIIHH', s)
    if key[0] == b'B' and key[1] == b'M' and len(key) == 10:
        print('The file is a bmp.\nThe size of photo: %d * %d\nThe number of colors: %d'
              % (key[6], key[7], key[9]))
    else:
        print('The file is not a bmp')