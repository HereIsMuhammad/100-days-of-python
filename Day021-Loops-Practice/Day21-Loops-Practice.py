# Day 21: Loop Practice (for & while)

# 1. for loop: print numbers 1 to 5

print("For loop: numbers 1 to 5")
for i in range(1, 6):
    print(i)


# 2. for loop: print even numbers from 1 to 10

print("For loop: even numbers from 1 to 10")
for num in range(1, 11):
    if num % 2 == 0:
        print(num)


# 3. while loop: print numbers 1 to 5

print("While loop: numbers 1 to 5")
x = 1
while x <= 5:
    print(x)
    x += 1


# 4. while loop: print odd numbers from 1 to 10

print("While loop: odd numbers from 1 to 10")
y = 1
while y <= 10:
    if y % 2 != 0:
        print(y)
    y += 1


# 5. for loop: sum of numbers from 1 to 5

print("Sum of numbers from 1 to 5")           
total = 0
for n in range(1, 6):       # total = 0 + 1  -> total = 1
                            #  total = 1 + 2  -> total = 3
                            #  total = 3 + 3  -> total = 6
                            #  total = 6 + 4  -> total = 10
                            #  total = 10 + 5 -> total = 15
    total = total + n                         

print("Sum =", total)

    