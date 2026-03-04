Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Arithmetic
a=4
b=6
a
4
b
6
print(a+b)
10
print(a-b)
-2
print(a*b)
24
print(a//b)
0
print(a/b)
0.6666666666666666
print(a%b)
4
print(a**b)
4096
b
6
a
4
#Assignment
a=2
b=4
a+=b
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
10
a-=b
a
6
a*=b
a
24
a//=b
a
6
a/=b
a
1.5
a+=1.5
a
3.0
a-=2
a
1.0
a*=4
a
4.0
a//=2
a
2.0
a/=1
a
2.0
a=8
b=2
b+=1
b
3
b-=1
b
2
b*=2
b
4
b/=1
b
4.0
b//=2
b
2.0
#Comparison
a=10
b=12
a
10
b
12
a<b
True
a>b
False
a<=b
True
a>=b
False
a==b
False
a!=b
True
b>a
True
b<a
False
b<=a
False
b>=a
True
b==a
False
b!=a
True
#logical
a=5
b=10
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a<=b or b>=a
True
a!=b or a==b
True
#identitfy
#identify
a=3
if type(a) is int:
    print("It is integer")

    
It is integer
if type(a) is float:
    print("It is int")

    


if type(a) is not floatL
SyntaxError: expected ':'
if type(a) is not float:
    print("It is int")

    
It is int
if type(a) is not int:
    print("It is int")

    


#membership
    
a=2,3,4,5,6,7,8,9
if 4 in a:
    print(4)

    
4
if 10 in a:
    print(10)

    


if 10 not in a:
    print(10)

    
10
#Bitwise
a=2
b=5
a&b
0
bin(2)
'0b10'
bin(5)
'0b101'
a=3
b=4
bin(a)
'0b11'
>>> bin(b)
'0b100'
>>> a&b
0
>>> a=3
>>> b=5
>>> bin(3)
'0b11'
>>> bin(5)
'0b101'
>>> a|b
7
>>> a=5
>>> ~b
-6
>>> a=5
>>> ~b
-6
>>> a=3
>>> b=6
>>> a^b
5
>>> bin(a)
'0b11'
>>> bin(b)
'0b110'
>>> a^b
5
