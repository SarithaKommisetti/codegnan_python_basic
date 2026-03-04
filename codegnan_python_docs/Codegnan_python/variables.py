Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Varibales
#variables
a=10
print(a)
10

==================================================================================== RESTART: Shell ====================================================================================
#variables
a=10
print(a)
10
print(7+8)
15
a=3
print(a)
3
b=7
c=9
print(b+c)
16
x=10
print(X)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
print(x)
10
Z=100
print(Z)
100
#donot start variables with a number
a2=10
print(a2)
10
a0123456789=200
print(a0123456789)
200
200
200
10x=400
SyntaxError: invalid decimal literal
#strings
start with upper or lower alpha
SyntaxError: invalid syntax
#start with upper or lower alpha
name="Saru"
print(name)
Saru
print("name")
name
city="Vizag"
print(city)
Vizag
Country="India"
print(Country)
India
#numbers
a=6;b=3
print(a+b)
9
a,b=5,6
print(a+b)
11
 a=12
 
SyntaxError: unexpected indent
_a=30
print(_a)
30
_=30
print(_)
30
#doesn't allow special chars
mail=saritha@gmail.com
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    mail=saritha@gmail.com
NameError: name 'saritha' is not defined
@a=3
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
mail="saritha@gmail.com"
print(mail)
saritha@gmail.com
data="saru@$1234"
print(data)
saru@$1234
#spaces
first name="Saritha"
SyntaxError: invalid syntax
firstname="Saritha"
print(firstname)
Saritha
first_name="Saritha"
print(first_name)
Saritha
fname="Saritha"
lname="Kommisetti"
print(fname+lname)
SarithaKommisetti

==================================================================================== RESTART: Shell ====================================================================================
print(fname+" "+lname)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    print(fname+" "+lname)
NameError: name 'fname' is not defined
fname="Saritha"
>>> lname="Kommisetti"
>>> print(fname+" "+lname)
Saritha Kommisetti
>>> print(fname,lname)
Saritha Kommisetti
>>> #del keyword
>>> a=12
>>> print(a)
12
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> #case sensitive
>>> Name="Saritha"
>>> print(Name)
Saritha
>>> NAME="Saritha"
>>> print(NaAME)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    print(NaAME)
NameError: name 'NaAME' is not defined. Did you mean: 'NAME'?
>>> NAME="Saritha"
>>> print(NAME)
Saritha
>>> name="Saritha"
>>> print(name)
Saritha
>>> #interpreting variables
>>> a=2
>>> print(a)
2
>>> x=20
>>> print(x)
20
>>> y=10
>>> print(x)
20
>>> print(y)
10
>>> #don't start with keywords
>>> if=20
SyntaxError: invalid syntax
