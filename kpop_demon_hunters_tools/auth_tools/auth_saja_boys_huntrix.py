import hashlib
import inquirer
import sys

# --- Reused Secure User Management Class ---
# (This part is identical and handles the logic and hashing)

class UserManager:
    def __init__(self):
        # Simulating a database with a dictionary
        self.users_db = {} 

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def signup(self, username, password):
        if username in self.users_db:
            print(f"❌ Error: User '{username}' already exists.")
            return False
        self.users_db[username] = self._hash_password(password)
        print(f"✅ Success: Account created for '{username}'.")
        return True

    def signin(self, username, password):
        if username not in self.users_db:
            print("❌ Error: Username not found.")
            return False
        if self.users_db[username] == self._hash_password(password):
            print(f"👋 Welcome back, {username}!")
            return True
        else:
            print("❌ Error: Incorrect password.")
            return False

    def change_password(self, username, old_password, new_password):
        if username not in self.users_db:
            print("❌ Error: User does not exist.")
            return False
        if self.users_db[username] == self._hash_password(old_password):
            self.users_db[username] = self._hash_password(new_password)
            print("✅ Success: Password updated successfully.")
            return True
        else:
            print("❌ Error: Old password was incorrect. Cannot update.")
            return False


# --- Dialog Flow Functions (Using inquirer) ---

def _run_signup_dialog(manager):
    """Handles the Sign Up input sequence."""
    questions = [
        inquirer.Text('username', message="Choose Username"),
        # Use Text for password input; the terminal will hide the input
        inquirer.Text('password', message="Choose Password") 
    ]
    answers = inquirer.prompt(questions)
    if answers:
        manager.signup(answers['username'], answers['password'])

def _run_signin_dialog(manager):
    """Handles the Sign In input sequence."""
    questions = [
        inquirer.Text('username', message="Enter Username"),
        inquirer.Text('password', message="Enter Password")
    ]
    answers = inquirer.prompt(questions)
    if answers:
        manager.signin(answers['username'], answers['password'])

def _run_change_password_dialog(manager):
    """Handles the Change Password input sequence."""
    questions = [
        inquirer.Text('username', message="Enter Username"),
        inquirer.Text('old_password', message="Enter Old Password"),
        inquirer.Text('new_password', message="Enter New Password")
    ]
    answers = inquirer.prompt(questions)
    if answers:
        manager.change_password(
            answers['username'], 
            answers['old_password'], 
            answers['new_password']
        )

# --- Main Program Loop ---

def run_auth_system():
    manager = UserManager()
    
    # Define the main menu list for inquirer
    questions = [
        inquirer.List(
            'action',
            message="🛡️ Player Authentication Menu 🛡️",
            choices=['1. Sign Up', '2. Sign In', '3. Change Password', '4. Exit'],
        )
    ]

    while True:
        # Prompt the user with the structured dialog menu
        answers = inquirer.prompt(questions)
        
        if answers is None:
            # Handle Ctrl+C or system interruption
            print("\nExiting system...")
            sys.exit()

        choice = answers['action']

        if '1. Sign Up' in choice:
            _run_signup_dialog(manager)
        elif '2. Sign In' in choice:
            _run_signin_dialog(manager)
        elif '3. Change Password' in choice:
            _run_change_password_dialog(manager)
        elif '4. Exit' in choice:
            print("Exiting system...")
            break

if __name__ == "__main__":
    run_auth_system()

