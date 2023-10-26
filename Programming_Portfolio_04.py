#One
Userinput = int(input("Enter a num: "))
def RangeCheck(Userinput):
    if Userinput <= 100 and Userinput >= 0:
        print("In Range")
    else:
        print("Not In Range")

RangeCheck(Userinput)

#Two
UserInput = input("Enter a string: ")
def CaseCheck(UserInput):
    U = 0
    L = 0
    for i in UserInput:
        if i.isupper():
            U += 1
        elif i.islower():
            L += 1
    print("Uppercase =",U,"\nLowercase =",L)

CaseCheck(UserInput)

#Three
Name = input("Enter your Name: ")
Name1 = Name[0].upper()
Name2 = Name[1:].lower()
print(Name1+Name2)

#Four
UserInput = input("Enter a string: ")
def RemLasCha(UserInput):
    if len(UserInput) > 1:
        print(UserInput[:-1])

RemLasCha(UserInput)
