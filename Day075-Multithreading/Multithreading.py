# Day 75: Multithreading

import threading
import time

# Task 1: Print numbers
def print_numbers():
    for i in range(1, 6):
        print("Number:", i)
        time.sleep(0.5)  # simulate delay

# Task 2: Print letters
def print_letters():
    for letter in ["A", "B", "C", "D", "E"]:
        print("Letter:", letter)
        time.sleep(0.5)  # simulate delay

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()

print("All threads finished!")