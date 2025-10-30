import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('clear' if os.name == 'posix' else 'cls')

def modern_cli():
    """A simple modern style CLI for entering names and ages."""
    clear_screen()
    print("===================================")
    print("  Huntrix Members Entry Interface  ")
    print("===================================
")

    members = []
    while True:
        name = input("Enter member name (or type 'exit' to quit): ").strip()
        if name.lower() == 'exit':
            break
        if not name:
            print("Name cannot be empty. Please try again.")
            continue

        age_input = input("Enter age: ").strip()
        if not age_input.isdigit() or int(age_input) <= 0:
            print("Invalid age. Please enter a positive number.")
            continue

        age = int(age_input)
        members.append({'name': name, 'age': age})
        print(f"Member '{name}' with age {age} added!
")

    print("
All entered members:")
    print("--------------------")
    if members:
        for i, m in enumerate(members, start=1):
            print(f"{i}. Name: {m['name']}, Age: {m['age']}")
    else:
        print("No members were entered.")

    print("
Thank you for using Huntrix Members Entry Interface!")

if __name__ == "__main__":
    modern_cli()
