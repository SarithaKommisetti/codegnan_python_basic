#a=["codegnan","python","course"]
#print(a.upper()) ->Raises an error

'''b=str(a)
print(b.upper())'''

'''for i in a:
    print(i.upper(),end=" ")'''

#syntax
#a=[expr for var in collection/range]
'''b=[i.upper() for i in a]
print(b)'''
    
'''a=["vij","hyd","vzg"]
b=[i.capitalize() for i in a]
print(b)'''

'''a=[2,4,5,6,8,12,13]
b=[i**2 for i in a]
print(b)'''

'''a=[2,4,5,6,8,12,13]
b=[i*i for i in a]
print(b)'''

'''a=[2,4,5,6,8,12,13]
b=[pow(i,2) for i in a]
print(b)'''

#if-usage in list-comprehension
'''a=int(input())
ls=[i for i in range(a) if i%2==0]
print(ls)'''

'''a=["apple","banana","mango","kiwi","berry","grapes"]
b=[i for i in a if i.startswith("a")]
print(b)'''

'''f=["apple","banana","mango","kiwi","berry","grapes"]
b=[i for i in f if "a" in i]
print(b)'''

#elif is not used in list comprehension 21-r e-sqrt o-mult

#if-else in list comprehension
'''ls=[i*i if i%2==0 else i*5 for i in range(21)]
print(ls)'''

a=[1,2,3,4,5]
b=[5,4,3,2,1] #[6,6,6,6,6]
'''ls=[]
for i,j in zip(a,b):
    ls.append(i+j)
print(ls)'''

'''lst=[i+j for i,j in zip(a,b)]
print(lst)'''

'''ls=[a[i]+b[i] for i in range(5)]
print(l)'''

'''l=[a[i]+b[i] for i in range(len(a))]
print(l)'''

#max,min,sum
a=[3,5,6,7,8,9,10,20,30]
print(max(a))
print(min(a))
print(sum(a))














