from math import sqrt
import cmath

operations = (input("do you want to perform a mathematical operation?: "))
print(" ")

if operations == "yes":
    print("OPERATIONS")
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. DIVISION")
    print("4. MULTIPLICATION")
    print("5. FIND THE AREA OF A TRIANGLE")
    print("6. FIND SQUARE ROOT")
    print("7. EXPONENTIATION")
    print("8. EXPONENTIATION 3 ")
    print("9. EXPONENTIATION 4 ")
    print("10. SOLVE A QUADRATIC EQUATION")
    print("11. SOLVE A SIMULTANEOUS EQUATION")
    print(" ")
    


        
    operation = int(input("select an operation to perform: "))

    if operation < 12:
        # The addition operation
        if operation == 1:
            print(" ")
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            num3 = int(input("Enter third number: "))
            sums = float(num1 + num2 + num3)
            print("The sum of ", num1, num2, "and", num3, " = ", sums)
        # The Subtraction operation
        elif operation == 2:
            print(" ")
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            sub = float(num1 - num2)
            print("The difference of ", num1, " and ", num2, " = ", sub)
        # The division operation
        elif operation == 3:
            print(" ")
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            div = float(num1 / num2)
            print("The division of ", num1, " by ", num2, " = ", div)
        # The multiplication operation
        elif operation == 4:
            print(" ")
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            mul = float(num1 * num2)
            print("The product of ", num1, " and ", num2, " = ", mul)
        # The operation for finding the area of a triangle operation
        elif operation == 5:
            print(" ")
            num1 = int(input("Enter the base number: "))
            num2 = int(input("Enter the height number: "))
            AOT = float(num1 * num2 / 2)
            print("The area of triangle base ", num1, "and height ", num2, " = ", AOT)
        # The operation for finding the square root of a constant
        elif operation == 6:
            print(" ")
            num1 = int(input("Enter the number you want to find the square root of: "))
            root = float(sqrt(num1))
            print("\u221A", num1, "=", root)

        # The operation for finding the power of a constant
        elif     operation == 7:
            print(" ")
            num1 = int(input("Enter the number you want to exponential: "))
            power = float(pow(num1, 2))
            print(num1, "\u00B2 = ", power)

        elif operation == 8:
            print(" ")
            num1 = int(input("Enter the number you want to exponential: "))
            power = float(pow(num1, 3))
            print("\u00B3", num1, "= ", power)

        elif operation == 9:
            print(" ")
            num1 = int(input("Enter the number you want to exponential: "))
            power = float(pow(num1, 4))
            print(num1, "\u2074 = ", power)

        # The operation for finding the solution of a quadratic equation
        elif operation == 10:
            print('General Form:- ax**2 + bx + c = 0')
            a = int(input('Enter a(a! = 0): '))
            b = int(input('Enter b: '))
            c = int(input('Enter c: '))
            
            d = (b**2)-(4*a*c)
            
            solution1 = (-b-cmath.sqrt(d))/(2*a)
            solution2 = (-b-cmath.sqrt(d))/(2*a)
            
            print('n')
            print(f"Results for equation, {a}x**2 + {b}x+{c} = 0, are in: ")
            
            if d > 0:
                print("Type of Roots: Two Distinct Real Roots")
            elif d == 0:
                print("Type of Roots: Two Real equal Roots")
            else:
                print("Type of Roots: Two Complex Roots")
            
            #The j represents a complex number in python
            print(f'The solutions are: {solution1} and {solution2}')
            

        elif operation == 11:
            print(" ")
            num1 = int(input("A: ")),
            num1 = int(input("B: ")),
            num1 = int(input("C: ")),
            power = float(num1, 4)
            print(power)

        else:
            print(" ")
            print("invalid Entry")
            print(" ")
            print(" ")
            
    operation += 1
    while operations == True:
        operations()

elif operations == "no":
    print(" ")
    print("Thank you for visiting...")

else:
    print(" ")
    print("You have entered an invalid input")
