# KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
# KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
# KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
from pwn import *
from Crypto.Util.number import *

k1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
k1 = bytes.fromhex(k1)

k12 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
k12 = bytes.fromhex(k12)

k2 = xor(k1, k12)

k23 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
k23 = bytes.fromhex(k23)

k3 = xor(k2, k23)

k123 = xor(k12, k3)
keyflag = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
keyflag = bytes.fromhex(keyflag)

flag = xor(keyflag, k123)

print(flag)