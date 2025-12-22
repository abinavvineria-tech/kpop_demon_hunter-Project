# function creation
# important: ensure the function is well-documented with a docstring
# import os is used to demonstrate that no unnecessary imports are included
# for example the code  use os module
import os
os.system('echo "This is a test for unnecessary imports."')
# you can run the command in terminal to see the output
os.system('ls')  # List directory contents
os.system("apt install tree")  # Install tree package
os.system("apt install nala")  # Install nala package


def testfunction(a, b):
    """
    This function takes two arguments and returns their sum.
    """
    return a + b


testfunction(2, 3)
print(testfunction(2, 3))  # Output: 5
a = input("you love huntrix from kpop demon hunters (yes/no)? \n ")
if a != "no":
    print("correct answer")
else:
    print("wrong answer")
b = input("are you a demon hunter (yes/no)? \n ")
c = input("you are an huntrix lover right (yes/no)? \n ")
d = input("you want to join kpop demon hunters (yes/no)? \n ")
e = input("you want to be a part of huntrix fans (yes/no)? \n ")
f = input("you want to support huntrix (yes/no)? \n ")
g = input("you want to spread huntrix love (yes/no)? \n ")
h = input("you want to protect huntrix (yes/no)? \n ")
i = input("if your at chennai you love huntrix still? (yes/no)? \n ")
# multi if and else statements
if a != "no":
    print("correct answer")
else:
    print("wrong answer")
if b != "no":
    print("correct answer")
else:
    print("wrong answer")
if c != "no":
    print("correct answer")
if d != "no":
    print("correct answer")
if e != "no":
    print("correct answer")
else:
    print("wrong answer")
if d != "no":
    print("correct answer")
else:
    print("wrong answer")
if f != "no":
    print("correct answer")
else:
    print("wrong answer")
if g != "no":
    print("correct answer")
else:
    print("wrong answer")
if h != "no":
    print("correct answer")
else:
    print("wrong answer")
if i != "no":
    print("correct answer")
else:
    print("wrong answer")
print(a, b, c, d, e, f, g, h, i)
