try:
  num = int(input("Enter a number:"))
  print(10/num)

except zerodivisionerror:
  print("Error: Division by zero is not allowed.")

except valueerror:
  print("Error: Invalid input. Please enter a valid integer.")
