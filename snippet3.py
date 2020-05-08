from operator import itemgetter
lst=[]
x=int(input("Enter the number of elements:"))
print("Enter the list elements:")
for i in range(0,x):
    b=input()
    lst.append(b)
    
print("The list is:"+str(lst))

print("Assigning elements from list")
p=int(input("Enter the first index to assign:"))
q=int(input("Enter the second index to assign:"))
r,s=itemgetter(p,q)(lst)
print("The assigned values are:"+str(r) +" " +str(s))
