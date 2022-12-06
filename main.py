import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def check(email):
    if re.fullmatch(regex, email):
        return True
    else:
        return False


while True:
    a = input("Enter Email Id (or q to exit): ")
    if a == "q":
        exit()
    if check(a) == False:
        print("Invalid Email Id...")
        print("*" * 100)
        print()
    else:
        bx = list(a.split("@"))
        print("User Name:", bx[0].lower())
        print("Domain Name: ", bx[1].upper())
        print("*" * 100)
        print()
