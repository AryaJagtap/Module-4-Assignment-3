______________________________________________________________________________
# Task 1: Calculate Factorial Using a Function 
'''
Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
'''
______________________________________________________________________________

num1 = int(input("Enter a number: "))
def factorial(num2):
    if num2 < 2 :
        return 1
    else:
        return num2 * factorial(num2 -1)

fact = factorial(num1)
print("Factorial of " + str(num1) + " is :", fact)
