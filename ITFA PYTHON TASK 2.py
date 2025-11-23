li=[120,89,77,200,510,100]
for x in li:
    if x > 500:
        break
    if x > 150:
        continue
    if x % 5==0:
        print(x)