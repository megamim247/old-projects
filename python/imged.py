import struct
with open('untitled.gif', 'rb') as f:
    data = bytearray(f.read())
pos = 10 + 1 * 2 + 1 * 4
data[pos:pos+3] = 255, 255, 255
print(data)
with open('eggs.bmp', 'wb') as f:
    f.write(data)
