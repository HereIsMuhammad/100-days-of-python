class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if not self.is_empty():
            removed = self.stack.pop()
            print(f"Popped: {removed}")
            return removed
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack:", self.stack)


# Testing
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

s.pop()
s.display()

print("Top element:", s.peek())