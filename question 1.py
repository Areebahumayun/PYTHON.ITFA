# Q1: Basic Mathematical Operations
a = int(input("Enter a: "))
b = int(input("Enter b: "))
operator = int(input("Enter operator (1 add, 2 subtract, 3 multiply): "))

if operator == 1:
    print(a + b, end= "")
elif operator == 2:
    print(a - b, end= "")
elif operator == 3:
    print(a * b, end= "")
else:
    print("Invalid Input", end= "")
