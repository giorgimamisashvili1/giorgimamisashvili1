# Task 1

age = int(input("How old are you: "))

if age < 15:
    print("you are kid")
elif age > 15 and age < 20:
    print("you are teenager")
else:
    print("you are grown")

# Task 2

num1 = 1

while num1 < 100:
    if num1 > 40 and num1 < 50:
        pass
    else:
        print(num1)
        num1 += 1