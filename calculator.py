while(1):
    a,b=list(map(float,input("Enter the two numbers:").split()))
    print("Which operations would you like to perform?")
    print("1.Addition (+)")
    print("2.Subtraction (-)")
    print("3.Multiplication (*)")
    print("4.Division (/)")
    choice=input()
    match choice:

        case "1"|"+":
            print(a, "+", b, "=",(a+b)) 
        case "2"|"-":
            print(a, "-", b, "=",a-b)
        case "3"|"*":
            print(a, "*", b, "=",a*b)
        case "4"|"/":
            if b==0:
                print("Undefined")
            else:
                print(a, "/", b, "=", a/b)
        case _:
            print("Invlid Input")
    cont=input("Do you want to continue(y/n):")
    if cont.lower()=='n':
        break
    
    
        
        