import re
def main():
    email = input("enter your mail:")
    check_mail(email)
    # name = input("enter your name:")
    # pehchan(name)

def check_mail(email):
    if re.search("^[^@]+@[^@]+\.com$",email):
        return print("Email Verified")
    else:
        return print("Invalid Email")
    
main()

# def pehchan(x):
#     if matches := re.search("^([a-zA-z]+), ([a-zA-z]+)$",x):
#         x = f"{matches.group(2)} {matches.group(1)}"
#     return print(f"Hello, {x}")
    
