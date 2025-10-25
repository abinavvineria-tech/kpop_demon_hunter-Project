#!/usr/bin/env python3
import time
import random
import os

# --- Data based on the "K-Pop Demon Hunters" movie ---
# HUNTR/X is a fictional 3-member girl group from the movie.
# Sources: KProfiles, K-Pop Demon Hunters Wiki

huntrx_group = {
    "name": "HUNTR/X (헌트릭스)",
    "fandom_name": "HUNTRs (Unofficial)",
    "debut": "June 20, 2025",
    "concept": "K-pop idols by day, demon hunters by night.",
    "members": [
        {
            "stage_name": "Rumi (루미)",
            "position": "Leader, Main Vocalist, Center",
            "weapon": "Saingeom (Divine Sword)",
            "status": "Ready for battle"
        },
        {
            "stage_name": "Mira (미라)",
            "position": "Vocalist, Demon Hunter",
            "weapon": "Celestial Fan",
            "status": "On standby"
        },
        {
            "stage_name": "Zoey (조이)",
            "position": "Vocalist, Demon Hunter",
            "weapon": "Spirit Bow",
            "status": "Scouting"
        }
    ]
}

demons_list = ["Gwi-Ma's Minion", "Saja Boy Imp",
               "Shadow Stalker", "Phantom", "Gaki", "Oni"]


def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_header():
    """Displays the main header for the CLI."""
    print("=" * 40)
    print("  K-POP DEMON HUNTERS - MANAGEMENT CLI")
    print("=" * 40)
    print(f"Group: {huntrx_group['name']}")


def display_menu():
    """Displays the main menu options."""
    print("--- Main Menu ---")
    print("1. View HUNTR/X Group Profile")
    print("2. View Member Profiles & Status")
    print("3. Start a Demon Hunt!")
    print("4. Exit")
    return input("Select an option (1-4): ")


def view_group_profile():
    """Displays detailed information about the group."""
    clear_screen()
    display_header()
    print("--- Group Profile ---")
    print(f"Group Name: {huntrx_group['name']}")
    print(f"Debut Date: {huntrx_group['debut']}")
    print(f"Fandom: {huntrx_group['fandom_name']}")
    print(f"Concept: {huntrx_group['concept']}")
    print(f"Total Members: {len(huntrx_group['members'])}")
    input("Press Enter to return to the menu...")


def view_member_profiles():
    """Displays profiles for each member of the group."""
    clear_screen()
    display_header()
    print("--- HUNTR/X Member Profiles ---")
    for i, member in enumerate(huntrx_group['members']):
        print(f"{i+1}. {member['stage_name']}")
        print(f"   Position: {member['position']}")
        print(f"   Weapon: {member['weapon']}")
        print(f"   Status: {member['status']}")
        input("Press Enter to return to the menu...")


def start_demon_hunt():
    """Simulates a demon hunt mission."""
    clear_screen()
    display_header()
    print("--- DEMON HUNT INITIATED ---")

    demon = random.choice(demons_list)
    hunter = random.choice(huntrx_group['members'])

    print(f"ALERT! A '{demon}' has appeared!")
    time.sleep(1.5)

    print(f"Dispatching hunter...")
    time.sleep(1)
    print(f"{hunter['stage_name']} is on the scene!")
    time.sleep(1.5)

    print(f"{hunter['stage_name']} readies her {hunter['weapon']}...")
    for i in range(3):
        print(".")
        time.sleep(0.7)

    success = random.choice([True, False, True])  # Higher chance of success

    if success:
        print(f"SUCCESS! {hunter['stage_name']} defeated the {demon}!")
        huntrx_group['members'][huntrx_group['members'].index(
            hunter)]['status'] = "Returning from mission"
    else:
        print(f"FAILED! The {demon} was too strong and escaped!")
        huntrx_group['members'][huntrx_group['members'].index(
            hunter)]['status'] = "Needs backup"

    input("Press Enter to return to the menu...")


def main():
    """Main function to run the CLI application."""
    while True:
        clear_screen()
        display_header()
        choice = display_menu()

        if choice == '1':
            view_group_profile()
        elif choice == '2':
            view_member_profiles()
        elif choice == '3':
            start_demon_hunt()
        elif choice == '4':
            print("Shutting down the system. Stay safe, hunters!")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 4.")
            time.sleep(1.5)


if __name__ == "__main__":
    main()
