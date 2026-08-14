# Day 63: To-Do List App

tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    print("Task added!")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nTo-Do List:")
    for i, t in enumerate(tasks):
        status = "✔" if t["completed"] else "✘"
        print(f"{i + 1}. {t['task']} [{status}]")


def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")


def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Deleted: {removed['task']}")
    else:
        print("Invalid task number.")


# Menu-driven program
while True:
    print("\n--- To-Do List App ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        view_tasks()
        num = int(input("Enter task number to complete: ")) - 1
        complete_task(num)

    elif choice == "4":
        view_tasks()
        num = int(input("Enter task number to delete: ")) - 1
        delete_task(num)

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")