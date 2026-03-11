#lists
      
a=[3,5,4,"saru",3+4j,True,False]
print(a)
#[3, 5, 4, 'saru', (3+4j), True, False]

#type()....
type(a)
#<class 'list'>
b=9
      
type(b)
#<class 'int'>

c=[9]
type(c)
#<class 'list'>

b=["python","c++","java"]
print(b)
#['python', 'c++', 'java']

#append()....
b.append(['html','css'])
print(b)
#['python', 'c++', 'java', ['html', 'css']]

#extend()....
b.extend(['html','css'])
print(b)
#['python', 'c++', 'java', ['html', 'css'], 'html', 'css']

c=['python', 'c++', 'java']
c.extend(['html', 'css'])
print(c)
#['python', 'c++', 'java', 'html', 'css']

#index()....
c.index('c++')
#1

#copy()....
c.copy()
#['python', 'c++', 'java', 'html', 'css']

d=c.copy()
print(d)
#['python', 'c++', 'java', 'html', 'css']

#clear()....
d.clear()
print(d)
#[]

#pop()....
a=["hi","hello","How","are","you?"]
a.pop()
#'you?'
print(a)
#['hi', 'hello', 'How', 'are']

print(a.pop(1))
#'hello'
      
#sort()....
b=['How', 'are', 'you']
b.sort()
print(b)
['How', 'are', 'you']

c=[2,45,1,0,14]
c.sort()
print(c)
#[0, 1, 2, 14, 45]

c.sort(reverse=True)
print(c)

#remove()....
c.remove(2)
print(c)
#[45, 14, 1, 0]

#len()....
d=["mango","kiwi","dragon"]
print(len(a))
#3

#count....
print(d.count("mango"))
#1
