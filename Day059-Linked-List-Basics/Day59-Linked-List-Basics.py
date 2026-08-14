# Day 59: Linked List Basics

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head

        if current is None:
            print("Linked List is empty")
            return

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# --- Testing ---
ll = LinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)

ll.display()