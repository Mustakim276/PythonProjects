#Gets input from user for variables
Num=int(input("Enter the number you would like to check:"))

#Checks if any number is divisible by the number from the user
for x in range(2,Num):
    if (Num % x) == 0:
        #Prints not a prime number if it finds a factor of Num
        print(Num,"is not a prime number.")
        break
#prints is a prime number if it passes the check
print(Num,"is a prime number.")