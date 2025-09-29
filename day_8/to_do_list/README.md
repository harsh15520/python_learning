## 1. Basic To-Do List (List + Functions)
This version uses a simple list and functions. You can add, view, edit, and delete tasks.

```python
# Basic To-Do List Manager

tasks = []

def display_menu():
    print("\n1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. View Tasks")
    print("5. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully.")

def edit_task():
    if tasks:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
        try:
            i = int(input("Enter task number to edit: ")) - 1
            if 0 <= i < len(tasks):
                new_task = input("Enter new task: ")
                tasks[i] = new_task
                print("Task edited successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks to edit.")

def delete_task():
    if tasks:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
        try:
            i = int(input("Enter task number to delete: ")) - 1
            if 0 <= i < len(tasks):
                tasks.pop(i)
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks to delete.")

def view_tasks():
    if tasks:
        print("\nCurrent Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("No tasks to show.")

while True:
    display_menu()
    choice = input("Select an option: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        edit_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        view_tasks()
    elif choice == '5':
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
```
## 2. Advanced To-Do List (Class-Based)
This version uses a class to encapsulate all the to-do list logic, making it more modular and easier to extend.

```python
class ToDoList:
    """Class to handle to-do list operations"""
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        print("\n1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")

    def add_task(self):
        task = input("Enter task: ")
        self.tasks.append(task)
        print("Task added successfully.")

    def edit_task(self):
        if self.tasks:
            self.display_tasks()
            try:
                i = int(input("Enter task number to edit: ")) - 1
                if 0 <= i < len(self.tasks):
                    new_task = input("Enter new task: ")
                    self.tasks[i] = new_task
                    print("Task edited successfully.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No tasks to edit.")

    def delete_task(self):
        if self.tasks:
            self.display_tasks()
            try:
                i = int(input("Enter task number to delete: ")) - 1
                if 0 <= i < len(self.tasks):
                    self.tasks.pop(i)
                    print("Task deleted successfully.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No tasks to delete.")

    def display_tasks(self):
        print("\nCurrent Tasks:")
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Select an option: ")
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.edit_task()
            elif choice == '3':
                self.delete_task()
            elif choice == '4':
                self.display_tasks()
            elif choice == '5':
                print("Exiting. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo = ToDoList()
    todo.run()
```
## 3. Further Extensions (For Practice)
- **Mark tasks as done:** Add a status to each task (e.g., a tuple or dictionary for each task).
- **Save/load tasks:** Use file I/O to persist tasks between runs.
- **Deadlines or priorities:** Store more info with each task.
- **GUI/Web version:** Try frameworks like Tkinter, Flet, or Django for a graphical/web interface.

***

**Summary:**
- Start with a list and functions for a basic to-do list.
- Use a class for better organization and scalability.
- Practice list methods (`append`, `pop`, direct indexing), user input, and error handling.
