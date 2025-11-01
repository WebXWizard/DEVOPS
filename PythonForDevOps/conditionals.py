
# Converting user input to lowercase

day_of_week = input("Enter the day of the week: ").lower()
print(f"You entered: {day_of_week}")

if day_of_week == "saturday" or day_of_week == "sunday": #true
    print("I will Learn DevOps on the weekend.")

else: #false
    print("I will Learn Python on a weekday.")


# Conditional statements in Python

num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

# Checking for even or odd
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# Simple Calculator using Conditionals

num1 = int(input("Please Enter Number1: "))
num2 = int(input("Please Enter Number2: "))

choice = input("Enter the operation :(Options +, -, *, /, %) ")

if choice == "+":
    sumOfNumbers = num1 + num2
    print("You selected Addition :", sumOfNumbers)
elif choice == "-":
    difference = num1 - num2
    print("You selected Subtraction :", difference)

elif choice == "*":
    product = num1 * num2
    print("You selected Multiplication :", product)

elif choice == "/":
    quotient = num1 / num2
    print("You selected Division :", quotient)

elif choice == "%":
    modulus = num1 % num2
    print("You selected Modulus :", modulus)
else:
    print("Invalid operation selected.")

# Using logical operators

age = int(input("Enter your age: "))
if age >= 18 and age <= 65:
    print("You are eligible to work.")
else:
    print("You are not eligible to work.")
