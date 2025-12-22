# this is how tto create a if and else statement in python and run a command using os module
import os
os.system("echo Hello, World!")
a = input("Do you want to continue? (yes/no): \n")
if a == "no":
    os.system("echo Goodbye!")
else:
    print("Continuing...")
b = input("Do you love huntrix from kpop demon hunters? (yes/no): \n")
if a != "yes" and b != "yes":
    os.system("echo You are missing out!")
else:
    print("Great choice!")
c = input("Do you want to exit now? (yes/no): \n")
if c == "yes":
    os.system("echo Exiting...")
else:
    print("Staying here...")
# create a multi line print function in python
print(a, "loves huntrix from kpop demon hunters")
print(b, "quittes missing out on huntrix from kpop demon hunters")
print(c, "quittes exiting the program")
