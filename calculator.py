a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
operation = input("Select operation (+ , - , * , / , ** , %, kg): ")

if operation == "+":
    print("Result:", a + b)

elif operation == "-":
    print("Result:", a - b)

elif operation == "*":
    print("Result:", a * b)

elif operation == "/":
    print("Result:", a / b)

elif operation == "**":
    print("Result:", a ** b )

elif operation == "%":
    print("Result:", ((a + b)*100)/200)

elif operation == "kg":
    print("Result:", a * 1000)

else:
    print("invalid operation")