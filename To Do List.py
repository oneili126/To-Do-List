## To Do List
tasks = []

def displayMenu():
    print("\n1. add a task, \n2. remove a task, \n3. print tasks, \n4. edit a task \n5. exit the application\n")
    user_selection = int(input("\nEnter selection\n"))
    selection = int(user_selection)
    if 1 <= selection <= 5:
        return selection
    return 0

def print_tasks():
    #prints the tasks in a numbered list
    if not tasks:
        print("No tasks yet.")
    else:
        print("\n")
        print("----------To Do----------")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")
        print("-------------------------")

#Title
print("\nWelcome to the To Do List App!")
print("----------------------------------")

while True:

    selection = displayMenu()

    if selection == 1:
        #Enter Task
        userTask = input("Enter the task: ")
        tasks.append(userTask)

    elif selection == 2:
        #Remove Selection
        print_tasks()
        if tasks:
            userTask = input("Enter the number of the task to be removed: ")
            if userTask.isdigit():
                taskNum = int(userTask)
                if 1 <= taskNum <= len(tasks):
                    tasks.pop(taskNum-1)
                else:
                    print("Invalid task number.")

    elif selection == 3:
        #Print Tasks
        print_tasks()

    elif selection == 4:
        #Edit Task
        print_tasks()
        if tasks:
            taskNum = int(input("Enter the number of the task to be edited: "))
        tempTask = input("Enter edit task:")
        tasks[taskNum-1] = tempTask
    elif selection == 5:
        # Exit Application
        exit(0)
        break
    else:
        #Ask them to enter a valid number
        print("Please Enter Valid Selection")
        
