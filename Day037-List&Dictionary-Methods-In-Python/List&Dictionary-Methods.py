# Day 37: List & Dictionary Methods in Python
# List Methods

## 1. append()

nums = [1, 2, 3]
nums.append(4)
print(nums)  # [1, 2, 3, 4]

## 2. extend()

a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)  # [1, 2, 3, 4]

## 3. insert()

nums = [10, 20, 30]
nums.insert(1, 15)
print(nums)  # [10, 15, 20, 30]

## 4. remove()

nums = [1, 2, 3, 2]
nums.remove(2)
print(nums)  # [1, 3, 2]

## 5. pop()

nums = [10, 20, 30]
x = nums.pop(1)
print(x)     # 20
print(nums)  # [10, 30]

## 6. clear()

nums = [1, 2, 3]
nums.clear()
print(nums)  # []

## 7. sort()

nums = [5, 2, 9, 1]
nums.sort()
print(nums)  # [1, 2, 5, 9]

## 8. reverse()

nums = [1, 2, 3]
nums.reverse()
print(nums)  # [3, 2, 1]

## 9. copy()

a = [1, 2, 3]
b = a.copy()
print(b)

# Dictionary Methods

## 1. keys(), values(), items()
student = {"name": "Ali", "age": 18, "class": 10}

print(student.keys())
print(student.values())
print(student.items())

## 2. get()

print(student.get("name"))
print(student.get("roll"))  # None (error nahi dega)

## 3. update()

student.update({"age": 19, "roll": 101})
print(student)

## 4. pop()

student.pop("age")
print(student)