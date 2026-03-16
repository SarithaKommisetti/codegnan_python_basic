#dicts

a={"name":"Saru","city":"RJY"}
print(a)
#{'name': 'Saru', 'city': 'RJY'}

print(a.keys())
#dict_keys(['name', 'city'])

print(a.values())
#dict_values(['Saru', 'RJY'])

print(a.items())
#dict_items([('name', 'Saru'), ('city', 'RJY')])

print(a["name"])
#'Saru'

a.update({"branch":"AI"},{"degree":"Mtech"})
'''Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.update({"branch":"AI"},{"degree":"Mtech"})
TypeError: update expected at most 1 argument, got 2'''

a.update({"state":"AP"})
print(a)
#{'name': 'Saru', 'city': 'RJY', 'state': 'AP'}

a.setdefault("Branch","AI")
#'AI'
print(a)
#{'name': 'Saru', 'city': 'RJY', 'state': 'AP', 'country': 'IND', 'continent': 'Asia', 'Branch': 'AI'}

b={"user":"Saritha","contact_no":9034839443,"mail_id":"saru@gmail.com"}
print(b)
#{'user': 'Saritha', 'contact_no': 9034839443, 'mail_id': 'saru@gmail.com'}

print(b.pop())
'''Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    b.pop()
TypeError: pop expected at least 1 argument, got 0'''

b.pop("mail_id")
'saru@gmail.com'
b
{'user': 'Saritha', 'contact_no': 9034839443}


a.update({"country":"IND","continent":"Asia"})
a
#{'name': 'Saru', 'city': 'RJY', 'state': 'AP', 'country': 'IND', 'continent': 'Asia'}

a.update({"branch":"AI"},{"degree":"Mtech"})
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.update({"branch":"AI"},{"degree":"Mtech"})
TypeError: update expected at most 1 argument, got 2
a.setdefault("Branch","AI")
'AI'
a
{'name': 'Saru', 'city': 'RJY', 'state': 'AP', 'country': 'IND', 'continent': 'Asia', 'Branch': 'AI'}

b={"user":"Saritha","contact_no":9034839443,"maik_id":"saru@gmail.com"}
print(b)
{'user': 'Saritha', 'contact_no': 9034839443, 'maik_id': 'saru@gmail.com'}
b.pop()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    b.pop()
TypeError: pop expected at least 1 argument, got 0
b.pop("mail_id")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    b.pop("mail_id")
KeyError: 'mail_id'
b.pop("maik_id")
'saru@gmail.com'
b
{'user': 'Saritha', 'contact_no': 9034839443}
n.popitem()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    n.popitem()
NameError: name 'n' is not defined
b.popitem()
('contact_no', 9034839443)
b
{'user': 'Saritha'}
b.copy()
{'user': 'Saritha'}
c={"time":1,"hour":2,"sec":5}
c
{'time': 1, 'hour': 2, 'sec': 5}
c.copy()
{'time': 1, 'hour': 2, 'sec': 5}
c.get("time")
1
c.get()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    c.get()
TypeError: get expected at least 1 argument, got 0
c.clear()
c
{}
c.len()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    c.len()
AttributeError: 'dict' object has no attribute 'len'
len(a)
6
x=["name":"Saru","city":"rjy","name":"saru"]
SyntaxError: invalid syntax
x={"name":"Saru","city":"rjy","name":"saru"}
x
{'name': 'saru', 'city': 'rjy'}
x={"name":"Saru","city":"rjy","name":"sari"}
x
{'name': 'sari', 'city': 'rjy'}
x={"name":"Saru","city":"rjy","name_1":"saru"}
x
{'name': 'Saru', 'city': 'rjy', 'name_1': 'saru'}
x={"names":["Saru","Mani"],"cities":["blr","chn"]}
x
{'names': ['Saru', 'Mani'], 'cities': ['blr', 'chn']}
x.keys()
dict_keys(['names', 'cities'])
x.values()
dict_values([['Saru', 'Mani'], ['blr', 'chn']])
x.items()
dict_items([('names', ['Saru', 'Mani']), ('cities', ['blr', 'chn'])])








