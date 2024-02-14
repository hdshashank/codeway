import csv
import os

# function to add tasks to the TO-DO list
def addtask(n):
    for i in range(n):
        task=['','']
        t=input("Enter the task to be added:")
        task[0]=t
        state="Incomplete"
        task[1]=state
        todo.append(task)
        print("Task was added successfully.")

# function to display tasks of the TO-DO list
def display():
    print("TO-DO LIST:")
    for index, val in enumerate(todo):
        print(index+1, val[0],val[1])

# function to edit tasks of the TO-DO list
def editask():
    display()
    ind=int(input("Enter the task to be edited:"))
    change=input("Enter the change to be made:")
    todo[ind-1][0]=change
    print("Task was edited successfully.")

# function to delete tasks of the TO-DO list
def deletetask():
    display()
    ind=int(input("Enter the S.No of task to be deleted:"))
    todo.pop(ind-1)
    print("Task was deleted successfully.")
    
# function to update tasks of the TO-DO list
def updatetask():
    display()
    ind=int(input("Enter the S.No of task whose status needs to be updated:"))
    if(todo[ind-1][1]=="Incomplete"):
        todo[ind-1][1]="Complete"
    elif(todo[ind-1][1]=="Complete"):
        todo[ind-1][1]="InComplete"
    print("Task",ind,"was marked completed successfully.")

# function to save TO-DO list in todo.csv file
def savetodo():
    with open(docname, 'w', newline="") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(todo) 
        file.close()

# function to clear the TO-DO list in todo.csv file
def cleartodo():
    with open(docname, 'w') as file:
        file.truncate()
        file.close()

todo=[]
# display the saved TO-DO list at the start of the program
docname="todo.csv"
rows = []
if os.stat(docname).st_size==0:
    print("\nEmpty TO-DO")
else:
    with open("todo.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            todo.append(row)
        for index, val in enumerate(todo):
            print(index+1, val[0],val[1])


while(1):
    print("\nFunctions:")
    print("1.Add Task")
    print("2.Display Tasks")
    print("3.Edit Task")
    print("4.Delete Task")
    print("5.Update Task Status")
    print("6.Save TO-DO")
    print("7.Clear TO-DO")
    print("8.Exit")
    choice=int(input("\nChoose the function you want to perform:"))
    match choice:
        case 1:
            n=int(input("\nEnter no. of tasks to be added:"))
            addtask(n)
        case 2:
            display()
        case 3:
            editask()
        case 4:
            deletetask()
        case 5:
            updatetask()
        case 6:
            savetodo()
        case 7:
            cleartodo()
        case 8:
            exit(0)
        case _:
            print("Invalid Input.")
