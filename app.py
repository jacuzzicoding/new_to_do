#The program will manage a to-do list with features:
# to add, remove, and mark tasks as completed, as well as view tasks.
#-------------------------

#defining the variables and functions
def tasks(task, date):
    return task, date


#welcoming message to user
print("Welcome to the To-Do List App!")
print("Please choose an option:")
print("1. Add a task\n2. Remove a task\n3. Mark a task as completed\n4. View tasks\n5. Exit")

#user input
option = int(input("Enter your option: "))
    if option == 1:
        task = input("Enter the task: ")
        date = input("Enter the date: ")
        tasks(task, date)