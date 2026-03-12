Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple()
a=(2,4.2,"d",3+4j,True,False)
print(a)
(2, 4.2, 'd', (3+4j), True, False)
type(a)
<class 'tuple'>
len(a)
6
a.index(True)
4
a.count(2)
1
#sets{}
a={1,3,2,"ef",4+6j,True}
a
{1, 2, 3, (4+6j), 'ef'}
a={1,3.2,"ef",4+6j,True}
print(a)
{1, 3.2, (4+6j), 'ef'}
a={1,3.2,"ef",6+7j,True}
a
{1, 3.2, (6+7j), 'ef'}
a.add(20)
a
{1, 3.2, 20, (6+7j), 'ef'}
a={1,2,3,4,5,6}
b={4,5,6}
a.add(20)
a
{1, 2, 3, 4, 5, 6, 20}
a.issubset(b)
False
b.issubset(a)
True
a.issuperset(b)
True
b.issuperset(a)
False
print(a.issuperset(b))
True
a={1,3.2,"ef",6+7j,True,False}
a
{False, 1, 3.2, (6+7j), 'ef'}
#union()
a={1,2,3,4,5}
b={4,5,6}
a.union(b)
{1, 2, 3, 4, 5, 6}
a.intersection(b)
{4, 5}
#difference()
a={1,2,3,4,5,6,7}
b={6,7,8,9,10,11,12}
a.difference(b)
{1, 2, 3, 4, 5}
b.difference(a)
{8, 9, 10, 11, 12}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
print(a.update(b))
None
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
x={4,5,6,1,2,3}
y={1,2,3,4,5,6}
x.inteersection(y)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    x.inteersection(y)
AttributeError: 'set' object has no attribute 'inteersection'. Did you mean: 'intersection'?
x.intersection(y)
{1, 2, 3, 4, 5, 6}
x.intersection_update(y)
x
{1, 2, 3, 4, 5, 6}
y.intersection_update(x)
y
{1, 2, 3, 4, 5, 6}
a={2,3,4,,6,7}
SyntaxError: invalid syntax
a={2,3,4,5,6,7}
b={1,2,3,4,,5,6,7,8,9}
SyntaxError: invalid syntax
a={2,3,4,5,6,7}
b={1,2,3,4,5,6,7,8,9}
a.difference_update(b)
a
set()
b.difference_update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9}
c={1,2,3,4,5,6,7}
d={5,6,7,8,9}
c.difference_update(d)
c
{1, 2, 3, 4}
d.difference_update(c)
d
{5, 6, 7, 8, 9}
a={3,4,5,6,7,8}
b={1,2,3,4,5,6}
a.symmetric_difference(b)
{1, 2, 7, 8}
b.symmetric_difference(a)
{1, 2, 7, 8}
print(a.symmetric_difference(b))
{1, 2, 7, 8}
a.symmetric_difference(b)
{1, 2, 7, 8}
a={10,20,30,40,50,60}
b={30,40,50,60,70,80,90}
a.symmetric_difference_update(b)
a
{70, 10, 80, 20, 90}
b.symmetric_difference_update(a)
b
{40, 10, 50, 20, 60, 30}
a={1,2,3,4,5}
b={4,5,6,7}
a.pop()
1
a.pop(3)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    a.pop(3)
TypeError: set.pop() takes no arguments (1 given)
a.remove(2)
a
{3, 4, 5}
a.copy()
{3, 4, 5}
a.clear()
a
set()
a={1,2,3,4,5}
>>> a.discard(4)
>>> a
{1, 2, 3, 5}
>>> len(a)
4
>>> a.index(3)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    a.index(3)
AttributeError: 'set' object has no attribute 'index'
>>> a.count(5)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    a.count(5)
AttributeError: 'set' object has no attribute 'count'
>>> a={1,2,3,5}
>>> b={4,5,6}
>>> a.isdisjoin(b)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    a.isdisjoin(b)
AttributeError: 'set' object has no attribute 'isdisjoin'. Did you mean: 'isdisjoint'?
>>> a.isdisjoint(b)
False
>>> a={1,2,3}
>>> b={1,2,3}
>>> a.isdisjoint(b)
False
