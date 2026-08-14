# Day 39: Variable Scope (Local & Global) in Python

print("=== Example 1: Local Variable ===")

def my_function():
    x = 10  # local variable
    print("Inside function, x =", x)

my_function()
# print(x)  # This will cause an error because x is local

print("\n=== Example 2: Global Variable ===")

y = 20  # global variable
def show():
    print("Inside function, y =", y)

show()
print("Outside function, y =", y)

print("\n=== Example 3: Same Name (Local vs Global) ===")

a = 5  # global variable
def test():
    a = 10  # local variable
    print("Inside function, a =", a)
test()
print("Outside function, a =", a)


print("\n=== Example 4: Using global keyword ===")

count = 0  # global variable
def increase():
    global count
    count = count + 1
    print("Inside function, count =", count)
increase()
print("Outside function, count =", count)


print("\n=== Example 5: Another global example ===")

name = "Ahmed"  # global variable
def greet():
    print("Hello,", name)
greet()
print("Name outside function:", name)



