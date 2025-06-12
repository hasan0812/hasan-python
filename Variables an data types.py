#WAP to input 2 numbers and print sum.
a = int(input("Enter first number"))
b = int(input("Enter second number"))
sum = a + b
print("sum is ",sum)

#WAP to input 2 numbers and print difference
H1 = int(input("Enter first number"))
H2 = int(input("Enter second number"))
if(H1 >= H2):
    diff = H1 - H2
    print("diff is ",diff)
elif(H2 > H1):
    diff = H1 - H2
    print("diff is ",diff)
else:
    print("activity end")      

