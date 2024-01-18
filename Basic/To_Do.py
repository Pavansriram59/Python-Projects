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
from datetime import date

def todo_list():

    # Maintaining a dictionary to store tasks
    tasks=[]
    task_number=0
    print("====== To-Do List ======")

    while True:
        
        print("\nOptions:")
        print("1.Display To-Do List")
        print("2.Add a Task")
        print("3.Mark a Task as completed")
        print("4.Remove a Task")
        print("5.Quit")
        choice=int(input("\nEnter a number to perform an operation:"))


        if(choice==1):
            print("\nYour Current Tasks are:")

            for task in tasks:
                print(f"Task {task['No.']}:{task['Name']}\nDate Added:{task['Date Added']}\nCompleted:{task['Completed']}\n")

        if(choice==2):
            task_number+=1
            new_task={
                "No.":task_number,
                "Name":input("Enter the task name to add:"),
                "Date Added":date.today(),
                "Completed":False
            }
            tasks.append(new_task)

        if(choice==3):
            for task in tasks:
                print(f"Task {task['No.']}:{task['Name']}\nDate Added:{task['Date Added']}\nCompleted:{task['Completed']}\n")
            
            num=int(input("Enter the task number to mark as completed:"))
            if num in [t["No."] for t in tasks]:
                tasks[num-1]["Completed"] = True
        
        if(choice==4):
            for task in tasks:
                print(f"Task {task['No.']}:{task['Name']}\nDate Added:{task['Date Added']}\nCompleted:{task['Completed']}\n")
            
            num=int(input("Enter the task number to remove:"))
            if num in [t["No."] for t in tasks]:
                tasks.remove(tasks[num-1])

        if(choice==5):
            break

todo_list()


