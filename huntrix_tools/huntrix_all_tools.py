#!/usr/bin/env python3
"""
Huntrix All Tools - Cross Platform Suite with Inquirer
"""

import os
import platform
import subprocess
import sys
import time
import inquirer

# Aura system state
aura = {
    "hunter_name": "Abinav",
    "aura_points": 100,
    "streak": 0,
    "quests_completed": 0
}

def system_info():
    print("\n=== System Info ===")
    print("OS:", platform.system(), platform.release())
    print("Machine:", platform.machine())
    print("Python:", platform.python_version())

def cube_timer():
    print("\n=== Cube Timer ===")
    input("Press Enter to start...")
    start = time.time()
    input("Press Enter to stop...")
    end = time.time()
    print("Solve Time:", round(end - start, 2), "seconds")

def file_manager():
    print("\n=== File Manager ===")
    path = input("Enter directory path: ")
    try:
        files = os.listdir(path)
        for f in files:
            print("-", f)
    except Exception as e:
        print("Error:", e)

def aura_system():
    print("\n=== Aura System ===")
    print("Hunter:", aura["hunter_name"])
    print("Aura Points:", aura["aura_points"])
    print("Streak:", aura["streak"])
    print("Quests Completed:", aura["quests_completed"])

def network_ping():
    print("\n=== Network Ping ===")
    host = input("Enter host (e.g., google.com): ")
    try:
        if platform.system() == "Windows":
            subprocess.run(["ping", host])
        else:
            subprocess.run(["ping", "-c", "4", host])
    except Exception as e:
        print("Error:", e)

def menu():
    while True:
        questions = [
            inquirer.List(
                "choice",
                message="Huntrix All Tools - Select an option",
                choices=[
                    "System Info",
                    "Cube Timer",
                    "File Manager",
                    "Aura System",
                    "Network Ping",
                    "Exit"
                ],
            ),
        ]
        answers = inquirer.prompt(questions)
        choice = answers["choice"]

        if choice == "System Info":
            system_info()
        elif choice == "Cube Timer":
            cube_timer()
        elif choice == "File Manager":
            file_manager()
        elif choice == "Aura System":
            aura_system()
        elif choice == "Network Ping":
            network_ping()
        elif choice == "Exit":
            print("Exiting Huntrix...")
            sys.exit(0)

        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    menu()
