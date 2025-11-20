# Q7: Smallest of Three Numbers
a, b, c = map(int, input("Enter three numbers: ").split())
if a <= b and a <= c:
    print("The smallest number is", a)
elif b <= a and b <= c:
    print("The smallest number is", b)
else:
    print("The smallest number is", c)


    # Q8: Positive, Negative, or Zero
n = int(input("Enter a number: "))
if n > 0:
    print("The number is positive")
elif n < 0:
    print("The number is negative")
else:
    print("The number is zero")