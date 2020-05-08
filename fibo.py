def recur(n):
    if n<=1:
        return n
    else:
        return(recur(n-1)+recur(n-2))
        
x=int(input("Enter any positive number:"))

if x<=0:
    print("please enter a positive number")
else:
    print("Fibonacci sequence is")
    for i in range(x):
        print(recur(i))
