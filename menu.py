import os
print("Press 1:to open chrome browser")
print("Press 2:to open notepad")
a=input("Enter choice:")

if int(a) == 1:
    os.system("start Chrome")
elif int(a) == 2:
    os.system("notepad")
else:
    print("Invalid input")
