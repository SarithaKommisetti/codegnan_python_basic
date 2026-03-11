#str methods
#len()
a="codegnan"
len(a)

c=""
len(c)

d=" "
len(d)

c1="twinkle twinkle little star"
c1.count(c1)
1

c1.count("twinkle")
2

c1.count("t")
5

a="python"
a.find("n")

a.index("n")

b="codegnan"
b.find("n")
5
b[5]+b[7]

#escape sequences
#\n -> new line
#\t -> tab  space
a="name\nmobileno\tmailid\ncity"
print(a)

a="name:Saritha\nmobileno:9846390247\tmailid:saru@gmail.com\ncity:RJY"
print(a)

#replace
a="wait until you succeed"
a.replace("wait","work")

b="wait wait until you succeed"
b.replace("wait","work")
b.replace("wait","work",1)

#upper()
a="hello"
a.upper()

#lower()
b="HI"
b.lower()

#capitalize
c="python"
c.capitalize()

#title
d="python course"
d.title()

#condition-checking

#isupper()
a.isupper()

#islower()
a.islower()

#startswith
a.startswith("c")

#endswith
a.endswith("e")

#isalpha
a.isalpha()

b="python course"
b.isalpha()

#isdigit()
c=1234

c.isdigit()
'''Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    c.isdigit()
AttributeError: 'int' object has no attribute 'isdigit' '''

#isalnum()
d="saru@123"
d.isalnum()

e="saru123"
e.isalnum()

#strip()-> remove left and right trailing spaces

a="  saritha kommisetti  "
a.strip()
#'saritha kommisetti'

#lstrip() -> remove left space
a.lstrip()
#'saritha kommisetti  '

#rstrip() -> remove right space
a.rstrip()
#'  saritha kommisetti'

#split()
a="python java c++"
a.split()
#['python', 'java', 'c++']

b="Hello world!"
b.split()
#['Hello', 'world!']

#join()
a="python","c++","java"
"".join(a)
#'pythonc++java'

" ".join(a)
#'python c++ java'

"#".join(a)
#'python#c++#java'


#concatenation
a="code"
b="gnan"
print(a+b)
#codegnan
a="python"
b="course"
print(a+b)
#pythoncourse
print(a+" "+b)
#python course

fname="saru"
lname="k"
print(fname+lname)
#'saruk'
print(fname+" "+lname)
#'saru k'
print(fname.title()+" "+lname.title())
#'Saru K'
print((fname+" "+lname).title())
'Saru K'

#formatting
a=3
b=6
print(a+b)
#9
print("the sum is", a+b)
#the sum is 9
print("the sum is a+b")
#the sum is a+b
city="vja"
print("the city is",city)
#the city is vja

#format method
a="motu"
b="patlu"
print("hello {}{}".format(a,b))
#hello motupatlu

print("hello {} {}".format(a,b))
#hello motu patlu

print("hello {} hello{}".format(a,b))
#hello motu hellopatlu

print("hello {} hello {}".format(a,b))
#hello motu hello patlu

#f-string
a="sita"
b="ram"
print(f'hello {a}{b}')
#hello sitaram

print(f"hello {a} {b}")
#hello sita ram

print(f"hello {a}hello{b}")
#hello sitahelloram

print(f"hello {a} hello{b}")
#hello sita helloram

print(f"hello {a} hello {b}")
#hello sita hello ram






'nn'
