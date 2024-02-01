import re

ip = input("Enter your ip address:")
c = 0
if match := re.search(r"^(.+)\.(.+)\.(.+)\.(.+)$",ip):
    arr = [match.group(1),match.group(2),match.group(3),match.group(4)]
    for i in arr:
        if int(i)>255:
            print("Invalid IP address")
            break;
        c = c+1
        if c == 4:
            print("IP Verified")            
else:
    print("Invalid IP address")