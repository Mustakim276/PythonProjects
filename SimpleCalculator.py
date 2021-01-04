#Gets input from user for variables
Num1=float(input("Enter the first number:"))
Num2=float(input("Enter the second number:"))
Operation=input("Enter the operation(+,-,*,/):")

#Determines what calculation to use from users input and outputs sum
if Operation == "+":
    print("Sum:" + str(Num1+Num2))
elif Operation == "-":
    print("Sum:" + str(Num1-Num2))
elif Operation == "*":
    print("Sum:" + str(Num1*Num2))
elif Operation == "/":
    print("Sum: " + str(Num1/Num2))