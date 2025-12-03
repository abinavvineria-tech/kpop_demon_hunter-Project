#!/bin/bash

# Kpop Demon Hunters Multi Tools (Dialog Version)
# Installs dialog if not present

# Install dialog
pkg install dialog -y

# Main menu
while true; do
  choice=$(dialog --title "Kpop Demon Hunters Multi Tools" \
    --menu "Choose an option:" 15 50 8 \
    1 "Update Termux" \
    2 "Upgrade Termux" \
    3 "Signup to Saja Boys & Huntrix" \
    4 "Change Password (Saja Boys & Huntrix)" \
    5 "Set New Password (Saja Boys & Huntrix)" \
    6 "Add Task (Taskwarrior)" \
    7 "Set Due Date (Taskwarrior)" \
    8 "Install Tool (Termux)" \
    9 "Send Notification (ntfy)" \
    10 "Exit" \
    3>&1 1>&2 2>&3)

  case $choice in
  1)
    dialog --msgbox "Updating Termux packages..." 10 40
    pkg update
    ;;
  2)
    dialog --msgbox "Upgrading Termux packages..." 10 40
    pkg upgrade
    ;;
  3)
    dialog --msgbox "Signup to Saja Boys and Huntrix groups (TODO)" 10 40
    ;;
  4)
    dialog --msgbox "Change password for Saja Boys and Huntrix (TODO)" 10 40
    ;;
  5)
    dialog --msgbox "Set new password for Saja Boys and Huntrix (TODO)" 10 40
    ;;
  6)
    task_desc=$(dialog --inputbox "Enter task description:" 10 40 3>&1 1>&2 2>&3)
    task add "$task_desc"
    dialog --msgbox "Task added!" 10 40
    ;;
  7)
    task_id=$(dialog --inputbox "Enter task ID:" 10 40 3>&1 1>&2 2>&3)
    due_date=$(dialog --inputbox "Enter due date (YYYY-MM-DD):" 10 40 3>&1 1>&2 2>&3)
    task $task_id modify due:$due_date
    dialog --msgbox "Due date set!" 10 40
    ;;
  8)
    tool_name=$(dialog --inputbox "Enter tool name:" 10 40 3>&1 1>&2 2>&3)
    pkg install $tool_name
    dialog --msgbox "Tool installed!" 10 40
    ;;
  9)
    msg=$(dialog --inputbox "Enter notification message:" 10 40 3>&1 1>&2 2>&3)
    curl -d "$msg" ntfy.sh/termux_main
    dialog --msgbox "Notification sent!" 10 40
    ;;
  10)
    dialog --msgbox "Exiting..." 10 40
    break
    ;;
  *)
    dialog --msgbox "Invalid option!" 10 40
    ;;
  esac
done
