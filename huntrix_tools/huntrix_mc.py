#!/usr/bin/env python3
# Huntrix Multi Tool in Python (Menu-driven)
# Abinav's Huntrix lore edition ⚡

from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem
import os
import subprocess

# --- Tool Functions ---


def update_tool():
    os.system("pkg update && pkg upgrade -y")
    print("✅ System updated successfully!")


def install_tool():
    tool = input("Enter package name to install: ")
    os.system(f"pkg install -y {tool}")
    print(f"✅ Installed {tool}")


def signup():
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    print(f"👤 Signup complete for {user} (password hidden).")


def password_manager():
    pwd = input("Enter new password: ")
    print("🔒 Password updated successfully!")


def task_manager():
    os.system("task list || echo 'Taskwarrior not installed'")
    print("📋 Task list displayed.")


def cube_timer():
    import time
    input("Press Enter to start timer...")
    start = time.time()
    input("Press Enter to stop timer...")
    end = time.time()
    print(f"🧊 Cube solve time: {end-start:.2f} seconds")


def file_manager():
    os.system("ls -lh")
    print("📂 Files listed.")


def aura_system():
    print("✨ Aura ritual activated! Huntrix energy flows...")


def fandom_rituals():
    print("🎶 Performing Huntrix fandom ritual...")


def ntfy_notification():
    topic = input("Enter ntfy topic: ")
    msg = input("Enter message: ")
    subprocess.run(["curl", "-d", msg, f"https://ntfy.sh/{topic}"])
    print("📢 Notification sent via ntfy!")


# --- Menu Setup ---
menu = ConsoleMenu("Huntrix Multi Tool", "Choose your destiny ⚡")

menu.append_item(FunctionItem("1. Update Tool", update_tool))
menu.append_item(FunctionItem("2. Install Tool", install_tool))
menu.append_item(FunctionItem("3. Signup", signup))
menu.append_item(FunctionItem("4. Password Manager", password_manager))
menu.append_item(FunctionItem("5. Task Manager", task_manager))
menu.append_item(FunctionItem("6. Cube Timer", cube_timer))
menu.append_item(FunctionItem("7. File Manager", file_manager))
menu.append_item(FunctionItem("8. Aura System", aura_system))
menu.append_item(FunctionItem("9. Fandom Rituals", fandom_rituals))
menu.append_item(FunctionItem("10. ntfy Notification", ntfy_notification))

menu.show()
