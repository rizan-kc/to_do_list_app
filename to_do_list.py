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
    pass

def delete_task():
    pass

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
