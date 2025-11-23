start=int (input("enter a starting range"))
end=int(input("enter an ending number"))

print("Prime numbers in given range are:")

for n in range(start, end + 1):
    if n > 1:  
        isprime = True
        for i in range(2, int(n**0.5) + 1):  
            if n % i == 0:
                isprime = False
                break
        if isprime:
            print(n, end=" ")