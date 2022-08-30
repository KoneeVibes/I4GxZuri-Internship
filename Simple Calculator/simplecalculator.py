from functions import * 


print ("What do you want to do?")
print ("1. Addition")
print ("2. Subtraction")
print ("3. Multiplication")
print ("4. Division")
print ("5. Modulus")

answer = float(input("enter your preffered action: "))

first_number = int(input("Enter the first number here:  "))
second_number = int(input("Enter the second number here:  "))

if answer == 1:
    result = addition(first_number,second_number)

elif answer == 2:
    subtraction(first_number, second_number)

elif answer == 3:
    multiplication(first_number, second_number)

elif answer == 4:
    division(first_number, second_number)

elif answer == 5:
    modulus (first_number, second_number)

else:
    print("Invalid Selection")
