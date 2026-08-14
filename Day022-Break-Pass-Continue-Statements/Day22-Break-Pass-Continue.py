# Day 22: Loop Control Statements

# 1. break statement
# Stops the loop when condition is met

for i in range(1, 11):
    if i == 6:
        break
    print(i)


# 2. continue statement
# Skips current iteration

print("Continue example (skip number 5):")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# 3. pass statement
# Does nothing (placeholder)

print("Pass example:")
for i in range(1, 6):
    if i == 3:
        pass
    print(i)


# 4. while loop with break

print("While loop with break:")
x = 1
while x <= 10:
    if x == 7:
        break
    print(x)
    x += 1

# 5. while loop with continue

print("While loop with continue (skip even numbers):")
y = 0
while y < 10:
    y += 1
    if y % 2 == 0:
        continue
    print(y)


