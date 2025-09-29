# Global list to store tasks
todo_list = []

class work_done:
    @staticmethod
    def view(to_list):
        print("--- Your To-Do List ---")
        if (to_list):
            for i in range(len(to_list)):
                print(f'{i+1}.{to_list[i]}')
        else:
            print("your to-do list is empty.")
    
    @staticmethod
    def add(to_list):
        user_input=input('enter task description: ')
        list_element=f"[ ] {user_input}"
        to_list.append(list_element)
        print(f'task {user_input} added succesfully!')
    
    @staticmethod
    def mark(to_list):
        work_done.view(to_list)
        if not to_list:
            return
        user_input=int(input('enter the number of the task to be marked as completed: '))
        if 1 <= user_input <= len(to_list):
            task_index = user_input - 1
            if to_list[task_index].startswith('[ ]'):
                to_list[task_index] = to_list[task_index].replace('[ ]', '[x]', 1)
                print(f'Task {user_input} marked as completed.')
            else:
                print(f'Task {user_input} is already completed.')
        else:
            print('Invalid task number.')
    
    @staticmethod
    def remove(to_list):
        work_done.view(to_list)
        if not to_list:
            return
        user_input=int(input('enter the number of task to be removed: '))
        if 1 <= user_input <= len(to_list):
            task_index = user_input - 1
            print(f'Task {to_list[task_index]} removed')
            to_list.pop(task_index)
        else:
            print('Invalid task number.')
while(True):
    print("--- Your To-Do List ---")
    print()
    print("0. View To-Do List \n1. Add a Task \n2. Mark a Task as Completed \n3. Remove a Task \n4. Exit \n")
    value=int(input('enter your choice (0-4): '))
    if(value==0):
        work_done.view(todo_list)
    elif(value==1):
        work_done.add(todo_list)
    elif(value==2):
        work_done.mark(todo_list)
    elif(value==3):
        work_done.remove(todo_list)
    elif(value==4):
        print("Exiting...")
        break
    else:
        print('invalid number')
