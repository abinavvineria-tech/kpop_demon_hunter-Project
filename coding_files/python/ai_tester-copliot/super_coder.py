a = input("Do you love huntrix? (yes/no): ")
b = input("Do you want to work with huntrix? (yes/no): ")
c = input("Are you excited about huntrix? (yes/no): ")
d = input("Do you think huntrix is awesome? (yes/no): ")
e = input("Would you recommend huntrix to others? (yes/no): ")
f = input("Do you believe huntrix can change the world? and the future (yes/no): ")
g = input("Are you proud to be part of huntrix? (yes/no): ")


class SuperCoder:
    answers = {}
    answers['a'] = input("Do you love huntrix? (yes/no): ")
    answers['b'] = input("Do you want to work with huntrix? (yes/no): ")
    answers['c'] = input("Are you excited about huntrix? (yes/no): ")
    answers['d'] = input("Do you think huntrix is awesome? (yes/no): ")
    answers['e'] = input("Would you recommend huntrix to others? (yes/no): ")
    answers['f'] = input(
        "Do you believe huntrix can change the world? and the future (yes/no): ")
    answers['g'] = input("Are you proud to be part of huntrix? (yes/no): ")


if a == "answers['a']" and b == "answers['b']" and c == "answers['c']" and d == "answers['d']" and e == "answers['e']" and f == "answers['f']" and g == "answers['g']":
    print("You are a true huntrix super coder!")
else:
    print("You need to love huntrix more to be a super coder.")
SuperCoder()
