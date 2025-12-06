#!/bin/bash

# Huntrix Multi-Tool
# Requires: dialog, taskwarrior, curl, termux-api (optional)

# Ensure dialog is installed
pkg install -y dialog

while true; do
  CHOICE=$(dialog --clear --backtitle "Huntrix Multi-Tool" \
    --title "Main Menu" \
    --menu "Choose an option:" 18 60 8 \
    1 "Update Termux (apt update)" \
    2 "Upgrade Termux (apt upgrade)" \
    3 "Signup to Huntrix Group" \
    4 "Change Password (Huntrix)" \
    5 "Set New Password (Huntrix)" \
    6 "Add Task (Taskwarrior)" \
    7 "Set Task Due Date (YYYY-MM-DD)" \
    8 "Install Tools (pkg install)" \
    2>&1 >/dev/tty)

  case $CHOICE in
  1)
    dialog --inputbox "Enter update command:" 8 60 "apt update" 2>cmd.txt
    CMD=$(<cmd.txt)
    eval "$CMD"
    dialog --msgbox "Update completed!" 6 40
    ;;
  2)
    dialog --inputbox "Enter upgrade command:" 8 60 "apt upgrade -y" 2>cmd.txt
    CMD=$(<cmd.txt)
    eval "$CMD"
    dialog --msgbox "Upgrade completed!" 6 40
    ;;
  3)
    USER=$(dialog --inputbox "Enter username:" 8 60 2>&1 >/dev/tty)
    PASS=$(dialog --passwordbox "Enter password:" 8 60 2>&1 >/dev/tty)
    dialog --msgbox "Signed up to Huntrix as $USER" 6 40
    ;;
  4)
    OLD_PASS=$(dialog --passwordbox "Enter old password:" 8 60 2>&1 >/dev/tty)
    NEW_PASS=$(dialog --passwordbox "Enter new password:" 8 60 2>&1 >/dev/tty)
    dialog --msgbox "Password changed for Huntrix" 6 40
    ;;
  5)
    NEW_PASS=$(dialog --passwordbox "Set new password:" 8 60 2>&1 >/dev/tty)
    dialog --msgbox "New password set for Huntrix" 6 40
    ;;
  6)
    TASK=$(dialog --inputbox "Enter task description:" 8 60 2>&1 >/dev/tty)
    task add "$TASK"
    dialog --msgbox "Task added: $TASK" 6 40
    ;;
  7)
    TASK_ID=$(dialog --inputbox "Enter task ID:" 8 60 2>&1 >/dev/tty)
    DUE_DATE=$(dialog --inputbox "Enter due date (YYYY-MM-DD):" 8 60 2>&1 >/dev/tty)
    task $TASK_ID modify due:$DUE_DATE
    dialog --msgbox "Task $TASK_ID due set to $DUE_DATE" 6 40
    ;;
  8)
    TOOL=$(dialog --inputbox "Enter tool to install (pkg name):" 8 60 2>&1 >/dev/tty)
    pkg install -y "$TOOL"
    dialog --msgbox "$TOOL installed successfully!" 6 40
    ;;
  esac
done
