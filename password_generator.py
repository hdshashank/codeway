import string
import random

def genpass(n):
    if(n>=6):
        password=''
        for i in range(n):
            password+=''.join(random.choice(pass_list))
        print(password)
    else:
        print("Password should have atleast 6 characters")


lower=list(string.ascii_lowercase)
upper=list(string.ascii_uppercase)
digits=list(string.digits)
symbols=list(string.punctuation)
pass_list=lower+upper+digits+symbols
n=int(input("Enter length(>6) of the password:"))
genpass(n)