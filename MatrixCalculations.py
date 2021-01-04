#Imports numpy library
import numpy as np

#Gets column size and contents for first matrix
Column1 = []
Column1input = int(input("Enter number of columns for the first matix: ")) 
  
for i in range(0, Column1input): 
    print("input a value for column",i+1)
    Column1ele = int(input()) 
  
    Column1.append(Column1ele)
   
#Gets row size and contents for first matrix
Row1 = []
Row1input = int(input("Enter number of rows for the first matix: ")) 
  
for i in range(0, Row1input): 
    print("input a value for row",i+1)
    Row1ele = int(input()) 
  
    Row1.append(Row1ele)

#Gets column size and contents for second matrix
Column2 = []
Column2input = int(input("Enter number of columns for the second matix: ")) 
  
for i in range(0, Column2input): 
    print("input a value for column",i+1)
    Column2ele = int(input()) 
  
    Column2.append(Column2ele)

#Gets row size and contents for secondmatrix
Row2 = []
Row2input = int(input("Enter number of rows for the second matix: ")) 
  
for i in range(0, Row2input): 
    print("input a value for row",i+1)
    Row2ele = int(input()) 
  
    Row2.append(Row2ele)

#Creates 2 new arrays from the users input
Array1 = np.array([[Row1],[Column1]])
Array2 = np.array([[Row2],[Column2]])

#Asks user what operation they would like to perform
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
Operation=int(input("Choose an operation:"))

#performs an operation depending on what the user selected
if Operation == 1:
    Output = np.add(Array1,Array2)
elif Operation == 2:
    Output = np.subtract(Array1,Array2)
elif Operation == 3: 
    Output = np.multiply(Array1,Array2)
else:
    print("You entered an invalid option.")

#Outputs resultant matrix
print(Output)