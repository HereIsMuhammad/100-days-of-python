# Day 54: Static & Class Methods

class Counter:
    count = 0   # class variable

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total objects created: {cls.count}")

    @staticmethod
    def message():
        print("Counter class is used to count objects.")


obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.show_count()
Counter.message()