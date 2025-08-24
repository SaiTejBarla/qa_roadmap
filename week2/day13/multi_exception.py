try:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    result = num1/num2
    print("Reslt:", result)

except ZeroDivisionError as e:
    print("Division by zero is not allowd")

except ValueError as e:
    print("Invalid input. Please enter a number.")

except Exception as e:
    print("An error occured:", str(e))