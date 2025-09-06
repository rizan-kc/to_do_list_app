def add():
    pass

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
