#now trying the if statement wich i have already tried multif times thus bro
age = int(input("enter your age: "))
if age>= 18:
    print("you are eligble for sign up")
elif age>=100:
    print("youa re too old to sign up: ")
elif age <18:
    print("you are not eligble for sign up: ")
elif age ==0:
    print("you are not born yet buddy")
else:
    print("please enter a valid age\n better luck next time buddy")

# now seeing a different type of example of buddy let's go bro.
user = input("hello\n do you wanst food y/N: ")
if user == "y":
    print("your food will be there in 13 minutes sir: ") 
else:
    print("get out from the resturant sir: ")
    
name = input("please enter your name sri: ")
if name == " ":
    print("you did not enter your name sir: ")
else:
    print(f"hello {name} \n have a good day sir")