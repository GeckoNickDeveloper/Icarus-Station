import array
import struct

msg = b'\x2c\x68\x3c\xc4\x9a\x32\x3e\xc3\x61\x18\x11\x45\xb7\xe4\xa7\xbc\x7c\xc6\x30\xbc\x80\x91\x19\x3d\x7d\x91\xb6\x3c\x17\xe9\xd6\xbd\x11\x7a\x56\x3f'
floats = array.array('f')
#floats.frombytes(msg, byteswap=True)

print(msg)
print("=====================")
#print(floats)

x = struct.unpack('<9f', msg)
print(x)

#print(len(msg[0:4]))
#print(struct.unpack('<f', msg[0:4]))
