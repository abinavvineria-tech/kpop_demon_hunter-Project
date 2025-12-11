import random
import inquirer
import sys

class HuntrixAura:
    def __init__(self, name="Huntrix Trainee"):
        self.name = name
        self.aura_level = 10  # Starting Aura
        self.stamina = 100    # Resource for training
        self.focus = 50       # Affects training efficiency

    def status(self):
        """Displays the current state of the trainee."""
        print(f"\n--- {self.name}'s Aura Status ---")
        print(f"  Aura Level: {self.aura_level}")
        print(f"  Stamina:    {self.stamina}%")
        print(f"  Focus:      {self.focus}/100")
        print("---------------------------------")
    
    def train_aura(self):
        """Attempts to increase Aura Level."""
        
        # Check if the trainee is too tired
        if self.stamina < 15:
            print("❌ Cannot train: Stamina is too low. Must rest first!")
            return

        # Training success is based on Focus
        focus_modifier = self.focus / 100
        aura_gain = random.randint(3, 7) * focus_modifier

        self.aura_level += round(aura_gain)
        self.stamina -= random.randint(10, 20)
        self.focus -= 5  # Training is mentally taxing
        
        print(f"\n✨ Aura training successful! Gained {round(aura_gain)} levels.")
        print(f"   Stamina decreased. Current Focus: {self.focus}.")

    def rest(self):
        """Restores stamina and slightly recovers focus."""
        stamina_gain = random.randint(30, 50)
        focus_gain = random.randint(5, 10)

        self.stamina = min(100, self.stamina + stamina_gain)
        self.focus = min(100, self.focus + focus_gain)
        
        print(f"\n💤 Resting completed. Stamina restored to {self.stamina}%.")
        
def run_aura_trainer():
    trainee = HuntrixAura("Rumi") # You can name your trainee here

    questions = [
        inquirer.List(
            'action',
            message="Choose your Aura Training Regimen",
            choices=['1. Train Aura (Cost: Stamina)', '2. Rest and Recover', '3. Check Status', '4. Exit Trainer'],
        )
    ]

    while True:
        trainee.status()
        
        # Display the interactive menu
        answers = inquirer.prompt(questions)
        
        if answers is None:
            # Handle Ctrl+C or interruption
            print("\nExiting Trainer...")
            sys.exit()

        choice = answers['action']

        if '1. Train Aura' in choice:
            trainee.train_aura()
        elif '2. Rest and Recover' in choice:
            trainee.rest()
        elif '3. Check Status' in choice:
            # Status is already shown before the menu, but provide an extra prompt.
            print("Status checked.")
            continue
        elif '4. Exit Trainer' in choice:
            print("\nTrainer shutting down. See you soon!")
            break

if __name__ == "__main__":
    run_aura_trainer()

