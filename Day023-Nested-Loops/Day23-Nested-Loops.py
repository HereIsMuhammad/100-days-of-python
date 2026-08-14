# For loop inside while loop

i = 1
while i <= 3:
    for j in range(1, 4):
        print(i, j)
    i += 1

# Nested while loop

i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(i, j)
        j += 1
    i += 1
