n=int(input("Enter the number of elements:"))
lst=[]
for i in range(0,n):
    b=int(input())
    
    lst.append(b)
    
print(lst)
out=[]
for i in range(0,n):
    if lst[i]>0:
        out.append(lst[i])
        
print(out)
