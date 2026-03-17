#Student Marks Analysis report
num=int(input("Enter the total number of students:"))
ls=[]
print("Display details:")
for i in range(num):
    marks=int(input())
    ls.append(marks)
print("Highest marks:",max(ls))
print("Lowest marks:",min(ls))
s=sum(ls)
n=len(ls)
avg=s/n
print("Total marks:",s)
print("Average marks:",avg)

    
