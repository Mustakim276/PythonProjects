#Gets input from user for variables
Num=int(input("Enter the number you would like to check:"))

print("The factors of",Num,"are:")

#checks for factors and outputs them
for x in range(1,Num + 1):
    if(Num % x == 0):
        print(x)