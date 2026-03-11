Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a="python course"
>>> print(a[-1:-8:-3])
eu 
>>> a[3:8:2]
'hnc'
>>> a[-6:-2:-1]
''
>>> a[8:3:2]
''
>>> #str methods
>>> #len()
>>> a="codegnan"
>>> len(a)
8
>>> b="python course"
>>> len(b)
13
>>> c=""
>>> len(c)
0
>>> d=" "
>>> len(d)
1
>>> #count()
c1="twinkle twinkle little star"
c1.count(c1)
1
c1.count("twinkle")
2
c1.count("t")
5
c1.count("k")
2
c1.count("z")
0
#find a string
a="python"
a.find("n")
5
a.index("n")
5
b="codegnan"
b.find("n")
5
b[5]+b[7]
'nn'
#escape sequences
#\n -> new line
#\t -> tab  space
a="name\nmobileno\tmailid\ncity"
print(a)
name
mobileno	mailid
city
a="name:Saritha\nmobileno:9846390247\tmailid:saru@gmail.com\ncity:RJY"
print(a)
name:Saritha
mobileno:9846390247	mailid:saru@gmail.com
city:RJY
#replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="wait until you succeed"
b="wait wait until you succeed"
b.replace("wait","work")
'work work until you succeed'
a.replace("wait","work",1)
'work until you succeed'
c="wait wait until you succeed"
c.replace("wait","work",1)
'work wait until you succeed'
#upper()
a="hello"
a.upper()
'HELLO'
b="HI"
b.lower()
'hi'
c="python"
c.capitalize()
'Python'
d="python course"
d.title()
'Python Course'
e="iam in class"
e.title()
'Iam In Class'
#condition-checking
a="code"
a.upper()
'CODE'
a.isupper()
False
a.islower()
True
a.startswith("c")
True
a.endswith("e")
True
a.isalpha()
True
b="python course"
b.isalpha()
False
b.isdigit()
False
c=1234
b.isdigit()
False
c.isdigit()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    c.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
d="saru@123"
d.isalnum()
False
e="saru123"
e.isalnum()
True
c="1234"
c.isnum()
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    c.isnum()
AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?


#strip()
#lstrip(),#rstrip()
a=" saritha kommisetti"
a.strip()
'saritha kommisetti'
a.lstrip()
'saritha kommisetti'
a="  saritha kommisetti  "
a.strip()
'saritha kommisetti'
a.lstrip()
'saritha kommisetti  '
a.rstrip()
'  saritha kommisetti'

#split()
a="python java c++"
a.split()
['python', 'java', 'c++']
b="Hello world!"
b.split()
['Hello', 'world!']

#join()
a="python","c++","java"
"".join(a)
'pythonc++java'
" ".join(a)
'python c++ java'
"#".join(a)
'python#c++#java'

#concatenation
a="code"
b="gnan"
print(a+b)
codegnan
a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "+b)
python course

fname="saru"
lname="k"
fname+lname
'saruk'
fname+" "+lname
'saru k'
fname.title()+" "+lname.title()
'Saru K'
(fname+" "+lname).title()
'Saru K'

#formatting
a=3
b=6
print(a+b)
9
print("the sum is", a+b)
the sum is 9
print("the sum is a+b")
the sum is a+b
city="vja"
print("the city is",city)
the city is vja
name="saru"
print("name is",name)
name is saru
print(sum(a,b))
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    print(sum(a,b))
TypeError: 'int' object is not iterable
a.add(b)
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    a.add(b)
AttributeError: 'int' object has no attribute 'add'

#format method
a="motu"
b="patlu"
print("hello {}{}".format(a,b))
hello motupatlu
print("hello {} {}".format(a,b))
hello motu patlu
print("hello {} hello{}".format(a,b))
hello motu hellopatlu
print("hello {} hello {}".format(a,b))
hello motu hello patlu
print(f'hello {a} {b}')
hello motu patlu

#f-string
a="sita"
b="ram"
print(f'hello {a}{b})
      
SyntaxError: unterminated f-string literal (detected at line 1)
print(f'hello {a}{b}')
      
hello sitaram
print(f"hello {a} {b}")
      
hello sita ram
print(f"hello {a}hello{b}")
      
hello sitahelloram
print(f"hello {a} hello{b}")
      
hello sita helloram
print(f"hello {a} hello {b}")
      
hello sita hello ram

#lists
      
a=[3,5,4,"saru",3+4j,True,False]
      
a
      
[3, 5, 4, 'saru', (3+4j), True, False]
type(a)
      
<class 'list'>
b=9
      
type(b)
      
<class 'int'>
c=[9]
      
type(c)
      
<class 'list'>
b=["python","c++","java"]
      
b
      
['python', 'c++', 'java']
b.append(['html','css'])
      
b
      
['python', 'c++', 'java', ['html', 'css']]
b.extend(['html'],'css')
      
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    b.extend(['html'],'css')
TypeError: list.extend() takes exactly one argument (2 given)
b.extend(['html','css'])
      
b
      
['python', 'c++', 'java', ['html', 'css'], 'html', 'css']
c=['python', 'c++', 'java']
      
c.extend(['html', 'css'])
      
c
      
['python', 'c++', 'java', 'html', 'css']

c.index('c++')
      
1
c.copy()
      
['python', 'c++', 'java', 'html', 'css']
d=c.copy()
      
d
      
['python', 'c++', 'java', 'html', 'css']
d.clear()
      
d
      
[]

#pop()
      
a=["hi","hello"]
      
a.pop()
      
'hello'
a
      
['hi']
a.pop(0)
      
'hi'
a
      
[]
a=["hi","hello","How","are","you?"]
      
a
      
['hi', 'hello', 'How', 'are', 'you?']
a.pop()
      
'you?'
a
      
['hi', 'hello', 'How', 'are']
a.pop(1)
      
'hello'
a
      
['hi', 'How', 'are']

a.sort()
      
a
      
['How', 'are', 'hi']
b=['How', 'are', 'you']
      
b.sort()
      
b
      
['How', 'are', 'you']
c=[2,45,1,0,14]
      
c.sort()
      
c
      
[0, 1, 2, 14, 45]
c.sort(reverse=True)
      
c
      
[45, 14, 2, 1, 0]
c.remove(2)
      
c
      
[45, 14, 1, 0]

d=["mango","kiwi","dragon"]
      
len(a)
      
3
d.count("mango")
      
1
