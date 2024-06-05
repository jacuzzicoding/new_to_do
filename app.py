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
    return True
# remove task
def remove_task(index):
    #check if the index is valid
    if 0 <= index < len(task_list):
         removed_task = task_list.pop(index)
         print("Removed task:", removed_task['task'])
    else:
        print("No tasks to remove!")
# mark task as completed 
def mark_task_completed(index):
    #check if the index is valid
    if 0 <= index < len(task_list):
        task_list[index]['status'] = 'completed'
        print("Task marked as completed:", task_list[index]['task'])
    else:
        print("No tasks to mark as completed!")
# view tasks (option 4)
def view_tasks():
     print("Here are your current tasks:")
     for index, task in enumerate(task_list):
        print(index, task['task'], task['date'], task['status'])
     if len(task_list) == 0:
        print("No tasks to display!")

#main loop starts here
print("Welcome to the To-Do List App!")
while True:
    print("\nPlease choose an option:")
    print("1. Add a task\n2. Remove a task\n3. Mark a task as completed\n4. View tasks\n5. Exit")

    #user input
    option = int(input("Enter your option: "))

    if option == 1:
            task = input("Enter the task: ")
            date = input("Enter the date (XX/XX/XXXX): ")
            add_task(task, date)
            view_tasks()
    elif option == 2:
            index = int(input("Enter the index of the task to remove: "))
            remove_task(index) 
    elif option == 3:
            index = int(input("Enter the index of the task to mark as completed: "))
            mark_task_completed(index)
    elif option == 4:
            view_tasks()
    elif option == 5:
        print("Exiting the To-Do List App. Have a great day!")
        break
    else:
        print("Invalid option. Please try again.")