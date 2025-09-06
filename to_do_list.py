def add():
    '''
    Adds new tasks to the to_do list.
    
    This function allows user to enter one or more tasks, where each 
    tasks are default assigned as In Progress. Then tasks are saved in 
    the task_list.txt file to keep them in track.

    task_file.txt - Stores tasks and statuses in formatted way.
                    Task_Name : Status

    '''
    tasks = {}
    while True:
        task = input("Enter your task: ").title()
        tasks[task] = "In Progress"

        add_more = input("Do you like to add more tasks? [y/n] ").lower()
        if add_more == 'y':
            continue
        else:
            break
    
    with open("tasks_list.txt","a") as f:
        for t in tasks:
            f.write(t + " : " + tasks[t] + "\n")
    

def mark_complete():
    while True:
        with open("tasks_list.txt","r") as f:
            x = f.readlines()
            task = dict() # using the dictionary to rewrite over the file
            for t in x:
                t = t.rstrip("\n")
                taskn,statusn = t.split(":")
                task[taskn.rstrip()] = statusn.lstrip()
            
        print(task)
        while True:
            task_to_mark = input("Enter the task, you want to mark as complete: ").title()
            if task_to_mark not in task:
                print("Invalid task to be marked!")
            else:
                task[task_to_mark] = "Completed"
                break
        with open("tasks_list.txt","w") as f:
            for t in task:
                f.write(t + " : " + task[t] + "\n") 
        print("Task marked as complete successfully!")
        option_mark = input("Do you want to mark another task as complete? [y/n]\n").lower()
        if option_mark == "y":
            continue
        else:
            break

def delete_task():
    while True:
        with open("tasks_list.txt","r") as f:
            x = f.readlines()
            task = dict() # using the dictionary to rewrite over the file
            for t in x:
                t = t.rstrip("\n")
                taskn,statusn = t.split(":")
                task[taskn.rstrip()] = statusn.lstrip()
            
        print(task)
        while True:
            task_to_delete = input("Enter the task, you want to delete: ").title()
            if task_to_delete not in task:
                print("No such task to be deleted!")
            else:
                task.pop(task_to_delete)
                break
        with open("tasks_list.txt","w") as f:
            for t in task:
                f.write(t + " : " + task[t] + "\n") 
        print("Task Deleted successfully!")
        option_mark = input("Do you want to delete another task? [y/n]\n").lower()
        if option_mark == "y":
            continue
        else:
            break

while True:

    print("\t\t\tWelcome To-Do List App")
    
    options = input("\nWhat would you like to do? [add/markcomplete/delete/quit] ").lower()

    if options == 'add':
        add()

    elif options == 'markcomplete':
        mark_complete()

    elif options == 'delete':
        delete_task()

    elif options == 'quit':
        print("\t\t\tThank you for using our app!")
        quit()
    else:
        print("Invalid option chosen!")
