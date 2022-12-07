from pwn import *
from Crypto.Util.number import *

x = "label"
x = [ord(o) for o in x]
print(x)
key = 13
print("".join(chr(key ^ o) for o in x))