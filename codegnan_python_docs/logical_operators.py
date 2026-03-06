#if-condition by using logical operators
'''a=3
b=6
if a<b and b>a:
    print("true")'''

'''a=3
b=6
if a<=b and b>=a:
    print("true")'''

'''a=3
b=6
if a<=b or a!=b:
    print("true")'''

'''a=3
b=6
if a==b or a>=b:
    print("true")'''

'''a=6
if not a==5:
    print("true")'''


#runtime_input
'''a=int(input())
b=int(input())
if a<=b and a!=b:
    print("true")'''

'''a=int(input())
b=int(input())
if a==b or a<=b:
    print("true")'''


'''a=int(input())
b=int(input())
if a<=b and a!=b:
    print("true")'''


'''a=int(input())
if not a!=5:
     print("true")'''

'''a="python"
b="java"
if a=="python" and b=="java":
    print("true")'''

'''a="python"
b="java"
if a=="python" or b=="java":
    print("true")'''

'''a="python"
b="java"
if not a=="python" :
    print("true")'''

'''a="python"
b="java"
if not a=="java":
    print("true")'''


#runtime_input
'''a=input("data1:")
b=input("data2:")
if a=="python" and b=="java":
    print("true")'''

'''a=input("data1:")
b=input("data2:")
if a=="java" and b=="python":
    print("true")'''

'''a=input("data1:")
b=input("data2:")
if a=="python" or b=="html":
    print("true")'''

'''a=input("data1:")
b=input("data2:")
if a==a and b==b:
    print("true")'''

#if-condition by using indentify operators
#is and isnot
'''a=5
if type(a) is int:
    print("false")

a=5
if type(a) is not int:
    print("false")

a=6.8
if type(a) is float:
    print("true")

a=6.8
if type(a) is not float:
    print("false")'''


'''a="python"
if type(a) is str:
    print("true")'''

'''a=4
if type(a) is not str:
    print("true")'''

'''a=3+4j
if type(a) is complex:
    print("true")'''

'''a=3+4j
if type(a) is not complex:
    print("true")'''

'''a=True
if type(a) is bool:
    print("true")'''

'''a=12
if type(a) is not bool:
    print("true")'''

'''a=1
if type(a) is bool:
    print("true")'''

#if-condition by using membership operators
'''a=[1,2,3,4,5,6,7,8,9]
if 8 in a:
    print("true")'''

'''a=[1,2,3,4,5,6,7,8,9]
if 10 not in a:
    print("false")'''

'''a=int(input())
if 3 in a:
    print("true")'''

'''a=[1,2,3,4,5,6,7,8,9]
b=int(input())
if b in a:
    print("true")'''

#if-else conditions by using logical operators
'''a=3
b=7
if a<b and b>a:
    print("true")
else:
    print("false")'''

'''a=3
b=7
if a<b or a>b:
    print("true")
else:
    print("false")'''

'''a=3
b=7
if not a<b and b>a:
    print("true")
else:
    print("false")'''

'''a=3
b=7
if not a<b or b>a:
    print("true")
else:
    print("false")'''

'''a=6
if type(a) is int:
    print("true")
else:
    print("false")'''

'''a=6
if type(a) is not int:
    print("true")
else:
    print("false")'''

'''a=3,4,5,6,7
if 5 in a:
    print("true")
else:
    print("false")'''

'''a=3,4,5,6,7
if 2 not in a:
    print("true")
else:
    print("false")'''
    
#if-elif

'''a=4
b=9
if a!=b:
    print("not equal")
elif a==b:
    print("equal")'''

'''a=4
b=9
if a==b:
    print("not equal")
elif a>=b:
    print("not equal")
elif a<b:
    print("true")'''

'''a=4
if type(a) is int:
    print("int")
elif type(a) is float:
    print("float")'''
'''a=4.2
if type(a) is int:
    print("int")
elif type(a) is not int:
    print("float")'''

'''a=2,3,4,5,6
if 4 in a:
    print("true")
elif 4 not in a:
    print("false")'''

'''a=2
b=3
if a==b and a<=b:
    print("true")
elif a<b or a>b:
    print("false")'''

#if-elif-else
'''a=10
b=20
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''

'''a=10
b=20
if a>b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''

'''a=10
b=20
if b<a:
    print("less")
elif a>b:
    print("greater")
else:
    print("true")'''

'''a=10
b=20
if a<b and b>a:
    print("less")
elif a<b or b>a:
    print("greater")
else:
    print("true")'''


'''a=6
if type(a) is int:
    print("true")
elif type(a) is not str:
    print("true")
else:
    print("false")'''

'''a=3,4,5,6,7
if 5 in a:
    print("true")
elif 2 not in a:
    print("false")    
else:
    print("false")'''

'''a="java"
b=2
if type(a) is str and type(b) is int:
    print("true")'''

#multiple-if
'''a=9
b=12
if a<b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''
'''a=9
b=12
if a==b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''

'''a=9
b=12
if a<b and a==b:
    print("less")
if b>a or a!=b:
    print("greater")
if not a!=b:
    print("not equal")'''

'''a=24
if type(a) is int:
	print("int")
if type(a) is float:
	print("float")
if type(a) is str:
	print("str")'''

'''a=2,3,4,5,6
if 3 in a:
	print("true")
if 7 not in a:
	print("true")
if 8 in a:
	print("true")'''









