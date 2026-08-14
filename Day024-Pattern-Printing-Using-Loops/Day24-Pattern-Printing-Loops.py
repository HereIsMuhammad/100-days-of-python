# 1. Square Pattern

for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()


# 2. Right Triangle Pattern

for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()


# 3. Number Pattern
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# 4. Same Number Pattern
for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()

