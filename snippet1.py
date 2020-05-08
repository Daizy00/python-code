#accessing elements from a tuple
tup1=(1,2,3,4,5)
tup2=("one","two","aplha","beta","delta")

x=int(input("Enter the index figure:"))

if x<0:
    print("Index can't be negative")
else:
    print("at index:"+str(x)," value of first tuple is:"+str(tup1[x]))
    print("at index:"+str
