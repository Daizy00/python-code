dictio={
    "Hello":20,
    "my":20,
    "name":30,
    "is":40,
    "Daizy":50
}
print("The original Dictionary is:"+str(dictio))
x=input("Enter any string:")

try:
    del dictio[x]
except KeyError:
    print(x,":not found")

print("Up
