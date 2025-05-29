#loop on array
fruits = ["Apple","banana","cherry"]
for x in fruits:
    print(x)
   
 #char loop
name = "python"
for char in name:
    print(char)

#while loop
count = 0
while count <5:
    print(count)
    count += 1

for i in range(1,4):
    for j in range(1,4):
        print ("*",end = " ")
        print(" ")

#print multiplication table
for i in range(1, 6): #outer loop for rows
    for j in range(1, 6): # inner loop for columns
        print(f"{i} x {j} = {i * j}", end="  ")
    print( ) #move to next line



    