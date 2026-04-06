to_do_list = []

def add_task(tasks_list):
    tasks = input("Enter Task: ")
    tasks_list.append(tasks)
    print("Your task has been added succesfully!")

def view_task(task_list):
    if not task_list:
        print("There are No Tasks.")
    else: 
        for i, task in enumerate(task_list, start=1):
            print(f"{i}. {task}")
        
def delete_task(index_num):
    view_task()
    index = int(input("Enter the task number that you want delete: "))
    index -= 1
    index_num.pop(index)
    print("Deleted SuccesfullY!")  

def edit_task(task_list):
    view_task(task_list)
    if not task_list:
        return
    
    index = int(input("Enter the task number that you want delete: "))
    index -= 1
    new_task = input("Enter new task: ")
    task_list[index] = new_task
    print("Task Updated Sucssfully!")

def save_task(task_list):
    with open("file.txt", "w") as file:
        for task in task_list:
            file.write(task + "\n")


def exit_app():
    print("Exited succesfully!")

while True:
    print("-----To-Do List-----")
    print("Choose an Option")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Edit Task")
    print("5. Exist")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Enter Vaild Option")
        continue
    
    if choice == 1:
        add_task(to_do_list)
    elif choice == 2:
        view_task(to_do_list)
    elif choice == 3:
        delete_task(to_do_list)
    elif choice == 4:
        edit_task(to_do_list)
    elif choice == 5:
        save_task(to_do_list)
    else:
        exit_app()
        break
