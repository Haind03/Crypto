from pwn import *
from Crypto.Util.number import *

x = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
x = bytes.fromhex(x)
print(x)
str = "crypto{"
str = str.encode()
key = xor(str, x)
print(key)
key = "myXORkey".encode()
flag = xor(key, x)
print(flag)