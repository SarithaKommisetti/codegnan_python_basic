Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # Datatypes
>>> a=4
>>> type(a)
<class 'int'>
>>> b=5.6
>>> type(b)
<class 'float'>
>>> c='code'
>>> type(c)
<class 'str'>
>>> d="code"
>>> type(d)
<class 'str'>
>>> e='''code'''
>>> type(e)
<class 'str'>
>>> f=True
>>> type(f)
<class 'bool'>
>>> g=False
>>> type(g)
<class 'bool'>
>>> f='p'
>>> type(f)
<class 'str'>
>>> d=4+9j
>>> type(d)
<class 'complex'>
>>> e=3j+7
>>> type(e)
<class 'complex'>
>>> h=3j
>>> type(h)
<class 'complex'>
>>> x=2+7i
SyntaxError: invalid decimal literal
>>> 2+7i
SyntaxError: invalid decimal literal
>>> x=Truw
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    x=Truw
NameError: name 'Truw' is not defined. Did you mean: 'True'?
>>> x=True
>>> type(x)
<class 'bool'>
y=False
type(y)
<class 'bool'>
x="true"
type(x)
<class 'str'>
#data type conversions
#int
int(4)
4
int(4.0)
4
int("saru")
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    int("saru")
ValueError: invalid literal for int() with base 10: 'saru'
int(2i+3j)
SyntaxError: invalid decimal literal
int(True)
1
int(False)
0
#float
float(1)
1.0
float(1.0)
1.0
float('saru')
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    float('saru')
ValueError: could not convert string to float: 'saru'
float(2i+3j)
SyntaxError: invalid decimal literal
float(True)
1.0
float(False)
0.0
#str
str(1)
'1'
str(1.0)
'1.0'
str('saru')
'saru'
str(saru)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    str(saru)
NameError: name 'saru' is not defined
str(2i+3j)
SyntaxError: invalid decimal literal
str(True)
'True'
str(False)
'False'
#cmplex
#complex
complex(4)
(4+0j)
complex(4.0)
(4+0j)
complex(2i+3j)
SyntaxError: invalid decimal literal
complex(2+3)
(5+0j)
complex(5i+4j)
SyntaxError: invalid decimal literal
complex('saru')
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    complex('saru')
ValueError: complex() arg is a malformed string
complex(True)
(1+0j)
complex(False)
0j
#boolean
bool(1)
True
bool(1.0)
True
bool(saru)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    bool(saru)
NameError: name 'saru' is not defined
bool('saru')
True
bool(2i+3j)
SyntaxError: invalid decimal literal
bool(True)
True
bool(False)
False
