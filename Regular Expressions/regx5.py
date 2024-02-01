import re
def main():
    time = input("Enter time in 12 hour format(Ex: 9 am to 10 pm / 9:00 am to 10:00 pm):").lower()
    convtime(time)
def convtime(x):
    if match := re.search(r"^(\d+)\:?(\d+)?\s(am|pm)\sto\s(\d+)\:?(\d+)?\s(am|pm)$",x):
        
        arr = []
        for i in match.groups():
            if i==None:
                arr.append("00")
            else:
                arr.append((i))

        if int(arr[0])<=12 and int(arr[3])<=12:
            if arr[2]=='pm':
                arr[0] = int(arr[0]) + 12
            if arr[5]=='pm':
                arr[3] = int(arr[3]) + 12
            print(f"{arr[0]}:{arr[1]} {arr[2]} to {arr[3]}:{arr[4]} {arr[5]}")

    else:
        print("Enter time in valid format")
main()