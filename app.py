#The program will manage a to-do list with features:
# to add, remove, and mark tasks as completed, as well as view tasks.
#-------------------------

#here is a global list I will use to store the tasks
task_list = []

#defining the variables and functions
# add task
def add_task(task, date):
    task_list.append({'task': task, 'date': date, 'status': 'incomplete'})
    print("The task,", task, ",added successfully!")
# remove task
def remove_task(index):
    #check if the index is valid
    if 0 <= index < len(task_list):
         removed_task = task_list.pop(index)
         print("Removed task:", removed_task['task'])
    else:
        print("No tasks to remove!")
# mark task as completed

#main loop starts here
print("Welcome to the To-Do List App!")
print("Please choose an option:")
print("1. Add a task\n2. Remove a task\n3. Mark a task as completed\n4. View tasks\n5. Exit")

#user input
option = int(input("Enter your option: "))
if option == 1:
        task = input("Enter the task: ")
        date = input("Enter the date (XX/XX/XXXX): ")
        add_task(task, date)