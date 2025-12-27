# new longest code ever written by huntrix_tools
zoey_friends = input("Enter zoey's friends from kpop demon hunters: ")
if zoey_friends == "rumi,mira" or zoey_friends == "mira,rumi":
    print("Correct! Zoey's friends are Rumi and Mira.")
else:
    print("Incorrect. Zoey's friends are Rumi and Mira.")
rumi_age = int(input("Enter Rumi's age: "))
zoey_age = int(input("Enter Zoey's age: "))
mira_age = int(input("Enter Mira's age: "))
if zoey_age < rumi_age and zoey_age > mira_age:
    print("Correct! Zoey is younger than Rumi but older than Mira.")
else:
    print("Incorrect. Zoey is younger than Rumi but older than Mira.")


class Friends_kpop_demon_hunters:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def zoeys_friends():
    rumi = Friends_kpop_demon_hunters("Rumi", rumi_age)
    zoey = Friends_kpop_demon_hunters("Zoey", zoey_age)
    mira = Friends_kpop_demon_hunters("Mira", mira_age)
    return [rumi, zoey, mira]


def display_friends(friends):
    for friend in friends:
        print(f"{friend.name} is {friend.age} years old.")
        print("Zoey's friends are Rumi and Mira.")
        friends = zoeys_friends()


if zoey_age == 22:
    print("Zoey is 22 years old.")
else:
    print("Zoey's age is not 22.")
if rumi_age == 23:
    print("Rumi is 23 years old.")
else:
    print("Rumi's age is not 23.")
if mira_age == 24:
    print("Mira is 24 years old.")
else:
    print("Mira's age is not 24.")


# check if the ages are correct via class instances
class AgeCheck:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_correct_age(self, correct_age):
        return self.age == correct_age


correct_ages = {"Zoey": 22, "Rumi": 23, "Mira": 24}
if (
    correct_ages["Zoey"] == zoey_age
    and correct_ages["Rumi"] == rumi_age
    and correct_ages["Mira"] == mira_age
):
    print("All ages are correct!")
else:
    print("Some ages are incorrect.")
zoey_friends_list = zoeys_friends()
display_friends(zoey_friends_list)
zoey = AgeCheck("Zoey", zoey_age)
rumi = AgeCheck("Rumi", rumi_age)
mira = AgeCheck("Mira", mira_age)
if zoey.is_correct_age(22):
    print("Zoey's age is verified as 22.")
else:
    print("Zoey's age verification failed.")
if rumi.is_correct_age(23):
    print("Rumi's age is verified as 23.")
else:
    print("Rumi's age verification failed.")
if mira.is_correct_age(24):
    print("Mira's age is verified as 24.")
else:
    print("Mira's age verification failed.")
confirmation = input(
    "Do you confirm that Zoey's friends are Rumi and Mira, and their ages are correct? (yes/no): "
)


class all_classes:
    def __init__(self, zoey_friends, zoey_age, rumi_age, mira_age):
        self.zoey_friends = zoey_friends
        self.zoey_age = zoey_age
        self.rumi_age = rumi_age
        self.mira_age = mira_age

    def confirm(self, confirmation):
        if confirmation.lower() == "yes":
            return "All information confirmed."
        else:
            return "Information not confirmed."
            all_info = all_classes(zoey_friends, zoey_age, rumi_age, mira_age)
        print(all_info.confirm(confirmation))
        if confirmation.lower() == "yes":
            print("Thank you for confirming Zoey's friends and their ages.")
        else:
            print("Please review the information about Zoey's friends and their ages.")


class LastCheck:
    def __init__(self, zoey_friends, zoey_age, rumi_age, mira_age):
        self.zoey_friends = zoey_friends
        self.zoey_age = zoey_age
        self.rumi_age = rumi_age
        self.mira_age = mira_age

    def final_verification(self):
        print("Final verification of Zoey's friends and their ages:")
        print(f"Zoey's friends: {self.zoey_friends}")
        print(f"Zoey's age: {self.zoey_age}")
        print(f"Rumi's age: {self.rumi_age}")


# print out the classes used in the code
Friends_kpop_demon_hunters("Zoey", zoey_age)
zoeys_friends()
all_classes(zoey_friends, zoey_age, rumi_age, mira_age)
final_check = LastCheck(zoey_friends, zoey_age, rumi_age, mira_age)
final_check.final_verification()
LastCheck(zoey_friends, zoey_age, rumi_age, mira_age)
final_check.final_verification()
print("End of Zoey's friends verification process.")
