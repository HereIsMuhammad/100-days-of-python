import multiprocessing
import time

# Task 1: Square numbers
def square_numbers():
    for i in range(1, 6):
        print(f"{i} squared = {i*i}")
        time.sleep(0.5)

# Task 2: Cube numbers
def cube_numbers():
    for i in range(1, 6):
        print(f"{i} cubed = {i**3}")
        time.sleep(0.5)

if __name__ == "__main__":
    # Create processes
    process1 = multiprocessing.Process(target=square_numbers)
    process2 = multiprocessing.Process(target=cube_numbers)

    # Start processes
    process1.start()
    process2.start()

    # Wait for processes to finish
    process1.join()
    process2.join()

    print("All processes finished!")