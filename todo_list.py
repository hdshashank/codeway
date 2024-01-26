def addtask(n):
    for i in range(n):
        task=input("Enter the task to be added:")
        todo.append(task)
        print("Task was added successfully.")

def display():
    print("TO-DO LIST:")
    for i in range(n):
        print(i+1,".",todo[i])

def editask():
    display()
    var=int(input("Enter the task to be edited:"))
    change=input("Enter the change to be made:")
    todo[var-1]=change
    print("Task was edited successfully.")

def deletetask():
    display()
    var=int(input("Enter the task to be deleted:"))
    todo.pop(var)
    print("Task was deleted successfully.")
    
def completetask():
    display()
    var=int(input("Enter the completed task:"))
    completetodo.append(todo[var])
    print("Task was marked completed successfully.")

todo=[]
completetodo=[]
while(1):
    print("Functions:")
    print("1.Add Task")
    print("2.Display Tasks")
    print("3.Edit Task")
    print("4.Delete Task")
    print("5.Complete Task")
    print("6.Exit")
    choice=int(input("Choose the function you want to perform:"))
    match choice:
        case 1:
            n=int(input("Enter no. of tasks to be added:"))
            addtask(n)
        case 2:
            display()
        case 3:
            editask()
        case 4:
            deletetask()
        case 5:
            completetask()
        case 6:
            exit(0)
        case _:
            print("Invalid Input.")
