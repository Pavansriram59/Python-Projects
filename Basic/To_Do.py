# * Basic To-Do Application

# 1. Display To-Do List:
#    - Enter '1' to display your current to-do list. It will show the tasks and their completion status.

# 2. Add a Task:
#    - Enter '2' to add a new task to your to-do list. You'll be prompted to enter the task's name.

# 3. Mark a Task as Completed:
#    - Enter '3' to mark a task as completed. You'll see the current list of tasks, and you'll be asked to enter the task number you want to mark as completed.

# 4. Remove a Task:
#    - Enter '4' to remove a task from your to-do list. You'll see the current list of tasks and will be prompted to enter the task number you want to remove.

# 5. Quit:
#    - Enter '5' to exit the application.

def todo_list():

    while True:

        # Maintaining a dictionary to store tasks
        d={1:"Hello Everyone"}
        
        print("Options:")
        print("1.Display To-Do List")
        print("2.Add a Task")
        print("3.Mark a Task as completed")
        print("4.Remove a Task")
        print("5.Quit")
        num=int(input("Enter a number to perform an operation:"))


        if(num==1):
            print("\nYour Current Tasks are : ")

            for k,v in d.items():
                print(k,".",v)

        if(num==2):
            s=input("Enter the task to add:")


