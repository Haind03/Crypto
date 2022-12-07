x = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
x = bytes.fromhex(x)
for i in range(len(x)):
    print("".join(chr(a ^ i) for a in x))
    