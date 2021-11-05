a = input("please enter your email : ")
def email(a):
    if "@" in a and "." in a :
        return True
    else:
        return False
if email(a) == True :
    print("valid")
else :
    print("not valid")
