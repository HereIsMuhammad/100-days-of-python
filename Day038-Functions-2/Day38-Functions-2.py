# Day 38: Functions 2


# 1. Default Arguments
def greet(name="User"):
    print("Hello", name)

greet("Ali")   # Hello Ali
greet()        # Hello User

# 2. Keyword Arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=18, name="Ahmed")

# 3. *args (Multiple Arguments)
def add(*numbers):
    total = 0
    for n in numbers:
        total += n
    print("Sum:", total)

add(1, 2, 3)
add(5, 10, 15, 20)

# 4. **kwargs (Key-Value Arguments)
def info(**data):
    for key, value in data.items():
        print(key, ":", value)

info(name="Ali", age=20, city="Lahore")

# 5. Return Multiple Values
def calc(a, b):
    add = a + b
    sub = a - b
    return add, sub

x, y = calc(10, 5)
print("Add:", x)
print("Sub:", y)

