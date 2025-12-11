#!/usr/bin/env python

import time
import random
import os
import inquirer
from termcolor import colored

# --- Configuration ---
LOG_FILE = "solves.txt"

# --- Scramble Generator ---
def generate_scramble(length=20):
    """Generates a simple 3x3 scramble."""
    moves = ["R", "R'", "R2", "L", "L'", "L2", "U", "U'", "U2", "D", "D'", "D2", "F", "F'", "F2", "B", "B'", "B2"]
    scramble = []
    
    # Simple logic to prevent opposite moves (e.g., R then R') 
    # and to limit consecutive turns on the same face.
    last_face = ""
    for _ in range(length):
        while True:
            move = random.choice(moves)
            current_face = move[0]
            if current_face != last_face:
                break
        scramble.append(move)
        last_face = current_face
    
    return " ".join(scramble)

# --- Timing and Logging Functions ---
def format_time(elapsed_seconds):
    """Formats seconds into M:SS.mmm string."""
    minutes = int(elapsed_seconds // 60)
    seconds = int(elapsed_seconds % 60)
    milliseconds = int((elapsed_seconds - int(elapsed_seconds)) * 1000)
    
    return f"{minutes:d}:{seconds:02d}.{milliseconds:03d}"

def log_solve(time_str):
    """Saves the solve time to the log file."""
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"{time_str}\n")
    except Exception as e:
        print(colored(f"\nError logging solve: {e}", "red"))

def run_timer():
    """Main timer loop logic."""
    os.system('clear')
    
    # 1. Display Scramble and instructions
    current_scramble = generate_scramble()
    print("=" * 50)
    print(colored("           ADVANCED CUBE TIMER", "cyan", attrs=["bold"]))
    print("=" * 50)
    print(colored("\nSCRAMBLE (3x3):", "yellow"))
    print(colored(f"   {current_scramble}", "white", attrs=["bold"]))
    print("-" * 50)
    
    print(colored("Press ENTER to START...", "green", attrs=["bold"]))

    # 2. START Timer
    input() # Wait for the first ENTER key press
    start_time = time.time()
    
    print(colored("\nTIMER RUNNING... (Press ENTER to STOP)", "magenta"))

    # 3. STOP Timer
    input() # Wait for the second ENTER key press
    stop_time = time.time()
    
    # 4. Calculate and Display Result
    elapsed_time = stop_time - start_time
    formatted_time = format_time(elapsed_time)
    
    # Log the time before displaying
    log_solve(formatted_time)

    os.system('clear')
    print("=" * 50)
    print(colored("           --- SOLVE COMPLETE ---", "cyan", attrs=["bold"]))
    print("=" * 50)
    print(f"Scramble: {current_scramble}")
    print(colored(f"\n   TIME: {formatted_time}", "green", attrs=["bold", "reverse"]))
    print("-" * 50)

# --- Main Program Loop ---
def main():
    while True:
        try:
            # Run the timer sequence
            run_timer()
            
            # Use inquirer for the restart/exit prompt
            questions = [
                inquirer.List(
                    'action',
                    message="What do you want to do next?",
                    choices=['New Solve', 'View Times', 'Exit'],
                    default='New Solve',
                )
            ]
            
            answers = inquirer.prompt(questions)
            
            if answers['action'] == 'Exit':
                print(colored("\nExiting Timer. Happy Cubing!", "red"))
                break
            elif answers['action'] == 'View Times':
                print(colored("\n--- SOLVE HISTORY ---", "yellow", attrs=["bold"]))
                try:
                    with open(LOG_FILE, "r") as f:
                        solves = f.readlines()
                        if solves:
                            for i, solve in enumerate(solves, 1):
                                print(f"{i}. {solve.strip()}")
                        else:
                            print("No solves logged yet.")
                except FileNotFoundError:
                    print("No solves logged yet.")
                
                input(colored("\nPress ENTER to continue to a new solve...", "blue"))
                
        except KeyboardInterrupt:
            print(colored("\n\nTimer interrupted. Exiting. Happy Cubing!", "red"))
            break
        except Exception as e:
            print(colored(f"\nAn unexpected error occurred: {e}", "red"))
            break

if __name__ == "__main__":
    main()


