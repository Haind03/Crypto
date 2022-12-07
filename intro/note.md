
# I. Khái niệm về `decode()` và `encode()`, `Encryption` và `Decryption`.

- `Encoding` là quá trình chuyển đổi chuỗi các ký tự như là chữ cái, chữ số và các ký tự đặc biệt thành một dạng format khác theo quy chuẩn nhất định (ví dụ như theo bảng mã ASCII) để truyền dẫn một cách hiệu quả.
- `Decoding` là quá trình chuyển đổi chuỗi ký tự đã bị encoding về lại trạng thái ban đầu. Quá trình này hoàn toàn khác với mã hóa - Encryption mà chúng ta vẫn hay lầm tưởng.

- Dữ liệu có thể được đọc và hiểu mà không cần bất kỳ biện pháp đặc biệt nào được gọi là plaintext, trong khi phương pháp ngụy trang plaintext để che giấu thông tin thực sự của nó được gọi là `Encryption` - mã hóa.
```
How Encryption Works?
Một thuật toán mã hóa hoạt động kết hợp với một key (key có thể là một chuỗi các ký tự, các con số) để mã hóa văn bản và cùng một văn bản sẽ được mã hóa thành các phiên bản khác nhau với các khóa khác nhau. Vì vậy, dữ liệu được mã hóa hoàn toàn phụ thuộc vào các tham số, ví dụ như độ mạnh của thuật toán mã hóa và tính bảo mật của khóa.

Đầu tiên chúng ta buộc phải sử dụng SSL certificate và install nó trên webserver. Nếu SSL không được sử dụng thì dữ liệu không thể được mã hóa. Một khi certificate được cài đặt, cần phải cấu hình cho server cốt để các pages sẽ hoạt động trên HTTPS - giao thức bảo mật thay vì HTTP version - giao thức không bảo mật.

Dữ liệu được mã hóa thường gọi là ciphertext và dữ liệu thông thường không được mã hóa thì gọi là plaintext. Khi user gửi một đoạn plaintext lên server, plaintext sẽ được mã hóa thành ciphertext nhờ public-key. Gói tin được đảm bảo an toàn và thông tin đã hoàn toàn được mã hóa trên đường truyền (encryption message). Sau đó, private-key sẽ đảm nhận nhiệm vụ giải mã nội dung gói tin. 2 loại khóa này đều được tạo nên từ những dãy số ngẫu nhiên. Public-key sẽ được chia sẻ với mọi người, nhưng Private-key phải được giữ bí mật, nó sẽ nằm hoàn toàn ở người có quyền giải mã. 2 key này hoạt động với nhiệm vụ hoàn toàn khác nhau. Như vậy khi người gửi tin nhắn mã hóa dữ liệu bằng public-key, và người nhận sẽ tiến hành giải mã bằng private-key và ngược lại.
```

- Plaintext được mã hóa được gọi là văn bản mã hóa và quá trình hoàn nguyên dữ liệu được mã hóa trở lại văn bản thuần túy được gọi là `Decryption` - giải mã.

# II. INTRODUCTION
## 1. Sử dụng python trong crypto

- `chr()` là hàm sử dụng để chuyển dạng hex về chữ trong bảng mã ascii
- `ord()` là hàm ngược lại với `chr()` 

```
import sys
chuoi = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

print("".join(chr(o) for o in chuoi))
```
- Flag : `crypto{ASCII_pr1nt4bl3}`

## 2. Mã hóa trong crypto

### 2.1 HEX

- Khi chúng ta mã hóa 1 thứ gì đó thì bản mã hóa chúng ta thu được sẽ không phải là các ký tự ASCII có thể in ra màn hình. Vì vậy nếu chúng ta muốn chia sẽ dự liệu đã mã hóa của mình, chúng ta sẽ mã hóa dữ liệu đó thành những thứ thân thiện với người dùng trên các loại hệ thống khác nhau. Có thể là dưới dạng chuỗi hex như ví dụ dưới đây :
- Chúng ta sẽ sử dụng `bytes.fromhex()` để chuyển các kí tự hex về dạng ascii có thể in ra màn hình.
- Ngược lại `bytes.hex()` sẽ chuyển các kí tự về dạng hex.

```

hexxa = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
x = bytes.fromhex(hexxa)
print(x)
x = bytes.hex(x)
print(x)
```

- Flag : ` b'crypto{You_will_be_working_with_hex_strings_a_lot}'`
```
b'crypto{You_will_be_working_with_hex_strings_a_lot}'
63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d
```

### 2.2 BASE64

- Một loại mã hóa phổ biến khác là base64, chúng cho phép biểu diễn dữ liệu nhị phân dưới dạng chuỗi ASCII sử dụng 64 ký tự. Một ký tự của chuỗi Base64 mã hóa 6 bit và do đó 4 ký tự của Base64 mã hóa ba byte 8 bit.
- Trong python có thư viện hỗ trợ cho base64 `import base64` trong đó ta sử dụng hàm `base64.b64encode()` để giải mã từ dạng ascii và ngược lại ta cũng có hàm `base64.b64decode()` để chuyển từ base64 về ngược lại ascii.
- Xem ví dụ dưới đây :

```
import base64
x = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
x = bytes.fromhex(x)
print(x)
x = base64.b64encode(x)
print(x)
x = base64.b64decode(x)
print(x)
```
- Sau khi chạy đoạn mã trên ta có được nội dung như sau :
```
b'r\xbc\xa9\xb6\x8f\xc1j\xc7\xbe\xeb\x8f\x84\x9d\xca\x1d\x8ax>\x8a\xcf\x96y\xbf\x92i\xf7\xbf'
b'crypto/Base+64+Encoding+is+Web+Safe/'
b'r\xbc\xa9\xb6\x8f\xc1j\xc7\xbe\xeb\x8f\x84\x9d\xca\x1d\x8ax>\x8a\xcf\x96y\xbf\x92i\xf7\xbf'
```


### 2.3 LIBRARY CRYPTO

- Cài đặt thư viện CRYPTO bằng lệnh sau: ` pip3 install pycryptodome
`
- Để sử dụng các hàm trong thư viện ta import thư viện bằng dòng lệnh `from Crypto.Util.number import *`
- Ngoài ra có 2 hàm thường sử dụng đó là `long_to_bytes()` và `bytes_to_long()` xem ví dụ dưới đây:

```
halston in ~/Crypto/Intro/Cr5 λ cat cr5.py
from Crypto.Util.number import *

x = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
x = long_to_bytes(x)
print(x)

halston in ~/Crypto/Intro/Cr5 λ python3 cr5.py
b'crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}'
```

### 2.4 XOR

 1. ví dụ về xor: Given the string "label", XOR each character with the integer 13. Convert these integers back to a string and submit the flag as crypto{new_string}

```
x = "label"
strig = [ord(o) for o in x]
print(strig)
print("".join((chr(13 ^ o) for o in strig)))
```
- Chúng ta thu được chuỗi mới
```
[108, 97, 98, 101, 108]
aloha
```
- Vậy Flag: `crypto{aloha}`

 2. XOR PROPERTIES
```
In the last challenge, you saw how XOR worked at the level of bits. In this one, we're going to cover the properties of the XOR operation and then use them to undo a chain of operations that have encrypted a flag. Gaining an intuition for how this works will help greatly when you come to attacking real cryptosystems later, especially in the block ciphers category.

There are four main properties we should consider when we solve challenges using the XOR operator

Commutative: A ⊕ B = B ⊕ A
Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
Identity: A ⊕ 0 = A
Self-Inverse: A ⊕ A = 0

Let's break this down. Commutative means that the order of the XOR operations is not important. Associative means that a chain of operations can be carried out without order (we do not need to worry about brackets). The identity is 0, so XOR with 0 "does nothing", and lastly something XOR'd with itself returns zero.

Let's try this out in action! Below is a series of outputs where three random keys have been XOR'd together and with the flag. Use the above properties to undo the encryption in the final line to obtain the flag.

KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
```

- Ta có đoạn code giải mã:
```
halston in ~/Crypto/Intro/CR7 λ cat cr7.py
# KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
# KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
from Crypto.Util.number import *
from pwn import *

key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key1_2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2_3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
key1_2_3 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

key2 = xor(bytes.fromhex(key1),bytes.fromhex(key1_2))
key3 = xor(key2, bytes.fromhex(key2_3))
key123 = xor(bytes.fromhex(key2_3),bytes.fromhex(key1))

flag = xor(key123,bytes.fromhex(key1_2_3))

print(flag.decode())
halston in ~/Crypto/Intro/CR7 λ python3 cr7.py
crypto{x0r_i5_ass0c1at1v3}
```

3. Favourite byte
```
# For the next few challenges, you'll use what you've just learned to solve some more XOR puzzles.

# I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.

# 73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d

x = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
x = bytes.fromhex(x)
for i in range(len(x)):
    print("".join(chr(i ^ o) for o in x))
    i += 1
    print("")

```
- Flag
```
sbi`dk h! O!%O}iOv$f eb!'#Ori'um
rchae~j!i !N $N|hNw%g!dc &"Nsh&tl
q`kbf}i"j#"M#'MkMt&d"g`#%!Mpk%wo
pajcg|h#k"#L"&L~jLu'e#fa"$ Lqj$vn
wfmd`{o$l%$K%!KymKr b$af%#'Kvm#qi
vgleazn%m$%J$ JxlJs!c%`g$"&Jwl"ph
udofbym&n'&I'#I{oIp"`&cd'!%Ito!sk
tengcxl'o&'H&"HznHq#a'be& $Hun rj
{jahlwc(`)(G)-GuaG~,n(mj)/+Gza/}e
zk`imvb)a()F(,Ft`F-o)lk(.*F{`.|d
yhcjnua*b+*E+/EwcE|.l*oh+-)Exc-g
xibkot`+c*+D*.DvbD}/m+ni*,(Dyb,~f
nelhsg,d-,C-)CqeCz(j,in-+/C~e+ya
~odmirf-e,-B,(BpdB{)k-ho,*.Bd*x`
}lgnjqe.f/.A/+AsgAx*h.kl/)-A|g){c
|mfokpd/g./@.*@rf@y+i/jm.(,@}f(zb
crypto{0x10_15_my_f4v0ur173_by7e}    <= this is flag
bsxqunz1y01^04^lx^g5w1ts062^cx6d|
ap{rvmy2z32]37]o{]d6t2wp351]`{5g
`qzswlx3{23\26\nz\e7u3vq240\az4f~
gv}tpk4|54[51[i}[b0r4qv537[f}3ay
fw|uqj~5}45Z40Zh|Zc1s5pw426Zg|2`x
etvri}6~76Y73YkY`2p6st715Yd1c{
du~wsh|767X62Xj~Xa3q7ru604Xe~0bz
kzqx|gs8p98W9=WeqWn<~8}z9?;Wjq?mu
j{py}fr9q89V8<VdpVo=9|{8>:Vkp>lt
ixsz~eq:r;:U;?UgsUl>|:x;=9Uhs=ow
hyr{dp;s:;T:>TfrTm?};~y:<8Tir<nv
o~u|xcw<t=<S=9SauSj8z<y~=;?Snu;iq
nt}ybv=u<=R<8R`tRk9{=x<:>Rot:hp
m|w~zau>v?>Q?;QcwQh:x>{|?9=Qlw9ks
l}v{`t?w>?P>:PbvPi;y?z}>8<Pmv8jr
SBI@D_KH☺o☺♣o]IoV♦FEB☺♥oRIUM
```

4. YOU EITHER KNOW, XOR YOU DON'T

- You either know, XOR you don't30 pts · 9717 Solves
- I've encrypted the flag with my secret key, you'll never be able to guess it. Remember the flag format and how it might help you in this challenge!
`0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104`

- Solutions
```
halston in ~/Crypto/Intro/cr9 λ cat exp.py
from pwn import *

x = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
x = bytes.fromhex(x)
key = xor(x, "crypto{".encode())
print(key)
flag = xor(x, "myXorkey".encode())
print(flag)
halston in ~/Crypto/Intro/cr9 λ python3 exp.py
b'myXORke+y_Q\x0bHOMe$~seG8bGURN\x04DFWg)a|\x1dTM!an\x7f'
b'cryPTo{1f_y\x10U_Kn0w_eN0uGH_y\x10U_Kn0w_\x11T_4ll}'
```

