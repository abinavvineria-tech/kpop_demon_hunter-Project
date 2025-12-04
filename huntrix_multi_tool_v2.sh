#!/bin/bash

# Huntrix Multi-Tool v2
# Supports both Termux and Linux

# Detect environment
detect_env() {
  if [ -d "/data/data/com.termux" ]; then
    ENV="termux"
    PKG_CMD="pkg"
  else
    ENV="linux"
    if command -v apt &>/dev/null; then
      PKG_CMD="sudo apt"
    elif command -v dnf &>/dev/null; then
      PKG_CMD="sudo dnf"
    elif command -v pacman &>/dev/null; then
      PKG_CMD="sudo pacman"
    else
      PKG_CMD="apt"
    fi
  fi
}

# Ensure dialog is installed
check_dialog() {
  if ! command -v dialog &>/dev/null; then
    echo "dialog is not installed. Installing..."
    if [ "$ENV" = "termux" ]; then
      pkg install -y dialog
    else
      $PKG_CMD install -y dialog 2>/dev/null || sudo apt install -y dialog
    fi
  fi
}

# User database files
SAJA_BOYS_DB="$HOME/.saja_boys_users"
HUNTRIX_DB="$HOME/.huntrix_users"

# Initialize
detect_env
check_dialog

# Main menu function
main_menu() {
  while true; do
    choice=$(dialog --clear --backtitle "Huntrix Multi-Tool v2 [$ENV]" \
      --title "Main Menu" \
      --menu "Choose an option:" 20 70 10 \
      1 "Update Repos [pkg update / apt update]" \
      2 "Install Tools [pkg install / apt install]" \
      3 "Sign Up on Groups (KPDH) [echo | sha256sum]" \
      4 "Sign In on Groups (KPDH) [grep]" \
      5 "Change Password (KPDH) [sed -i]" \
      6 "Set Notification (ntfy) [curl ntfy.sh]" \
      7 "Add Task (Taskwarrior) [task add]" \
      8 "Set Task Due Date (Taskwarrior) [task modify]" \
      9 "Exit" \
      2>&1 >/dev/tty)

    if [ $? -eq 1 ]; then
      clear
      exit 0
    fi

    case $choice in
    1) update_repos ;;
    2) install_tools ;;
    3) signup_groups ;;
    4) signin_groups ;;
    5) change_password_groups ;;
    6) set_notification ;;
    7) add_task ;;
    8) due_task ;;
    9) clear; exit 0 ;;
    *) clear; exit 0 ;;
    esac
  done
}

# Update Repos function
update_repos() {
  dialog --infobox "Updating repositories..." 5 40
  sleep 1
  
  if [ "$ENV" = "termux" ]; then
    output=$(pkg update -y 2>&1)
  else
    if command -v apt &>/dev/null; then
      output=$(sudo apt update 2>&1)
    elif command -v dnf &>/dev/null; then
      output=$(sudo dnf check-update 2>&1)
    elif command -v pacman &>/dev/null; then
      output=$(sudo pacman -Sy 2>&1)
    else
      output="No supported package manager found."
    fi
  fi
  
  dialog --title "Update Complete" --msgbox "$output" 20 70
}

# Install Tools function
install_tools() {
  tool=$(dialog --inputbox "Enter tool name to install:" 8 50 2>&1 >/dev/tty)
  if [ $? -eq 1 ] || [ -z "$tool" ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  
  dialog --infobox "Installing $tool..." 5 40
  
  if [ "$ENV" = "termux" ]; then
    output=$(pkg install -y "$tool" 2>&1)
  else
    if command -v apt &>/dev/null; then
      output=$(sudo apt install -y "$tool" 2>&1)
    elif command -v dnf &>/dev/null; then
      output=$(sudo dnf install -y "$tool" 2>&1)
    elif command -v pacman &>/dev/null; then
      output=$(sudo pacman -S --noconfirm "$tool" 2>&1)
    else
      output="No supported package manager found."
    fi
  fi
  
  dialog --title "Install Output" --msgbox "$output" 20 70
}

# Select Group function
select_group() {
  group=$(dialog --clear --backtitle "KPDH Groups" \
    --title "Select Group" \
    --menu "Choose a group:" 12 50 2 \
    1 "Saja Boys" \
    2 "Huntrix" \
    2>&1 >/dev/tty)
  
  if [ $? -eq 1 ]; then
    echo ""
    return
  fi
  
  case $group in
  1) echo "saja_boys" ;;
  2) echo "huntrix" ;;
  *) echo "" ;;
  esac
}

# Get DB file for group
get_group_db() {
  case "$1" in
  "saja_boys") echo "$SAJA_BOYS_DB" ;;
  "huntrix") echo "$HUNTRIX_DB" ;;
  esac
}

# Get display name for group
get_group_name() {
  case "$1" in
  "saja_boys") echo "Saja Boys" ;;
  "huntrix") echo "Huntrix" ;;
  esac
}

# Sign Up on Groups function
signup_groups() {
  group=$(select_group)
  if [ -z "$group" ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  
  db_file=$(get_group_db "$group")
  group_name=$(get_group_name "$group")
  
  username=$(dialog --inputbox "Enter your $group_name username:" 8 50 2>&1 >/dev/tty)
  if [ $? -eq 1 ] || [ -z "$username" ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  
  password=$(dialog --insecure --passwordbox "Enter your password:" 8 50 2>&1 >/dev/tty)
  if [ $? -eq 1 ] || [ -z "$password" ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  
  confirm=$(dialog --insecure --passwordbox "Confirm password:" 8 50 2>&1 >/dev/tty)
  if [ $? -eq 1 ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  
  if [ "$password" != "$confirm" ]; then
    dialog --msgbox "Passwords do not match!" 6 40
    return
  fi
  
  if grep -q "^$username:" "$db_file" 2>/dev/null; then
    dialog --msgbox "Username already exists in $group_name. Please choose another." 6 50
    return
  fi
  
  hashed=$(echo "$password" | sha256sum | awk '{print $1}')
  echo "$username:$hashed" >> "$db_file"
  dialog --msgbox "Registration successful for '$username' in $group_name!" 6 50
}

# Sign In on Groups function
signin_groups() {
  group=$(select_group)
  if [ -z "$group" ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  
  db_file=$(get_group_db "$group")
  group_name=$(get_group_name "$group")
  
  username=$(dialog --inputbox "Enter your $group_name username:" 8 50 2>&1 >/dev/tty)
  if [ $? -eq 1 ] || [ -z "$username" ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  
  password=$(dialog --insecure --passwordbox "Enter your password:" 8 50 2>&1 >/dev/tty)
  if [ $? -eq 1 ] || [ -z "$password" ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  
  hashed=$(echo "$password" | sha256sum | awk '{print $1}')
  
  if grep -q "^$username:$hashed$" "$db_file" 2>/dev/null; then
    dialog --msgbox "Sign in successful! Welcome, $username to $group_name!" 6 50
  else
    dialog --msgbox "Login failed. Invalid username or password." 6 50
  fi
}

# Change Password on Groups function
change_password_groups() {
  group=$(select_group)
  if [ -z "$group" ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  
  db_file=$(get_group_db "$group")
  group_name=$(get_group_name "$group")
  
  username=$(dialog --inputbox "Enter your $group_name username:" 8 50 2>&1 >/dev/tty)
  if [ $? -eq 1 ] || [ -z "$username" ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  
  old_password=$(dialog --insecure --passwordbox "Enter your old password:" 8 50 2>&1 >/dev/tty)
  if [ $? -eq 1 ] || [ -z "$old_password" ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  
  old_hashed=$(echo "$old_password" | sha256sum | awk '{print $1}')
  
  if ! grep -q "^$username:$old_hashed$" "$db_file" 2>/dev/null; then
    dialog --msgbox "Invalid username or password." 6 50
    return
  fi
  
  new_password=$(dialog --insecure --passwordbox "Enter new password:" 8 50 2>&1 >/dev/tty)
  if [ $? -eq 1 ] || [ -z "$new_password" ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  
  confirm=$(dialog --insecure --passwordbox "Confirm new password:" 8 50 2>&1 >/dev/tty)
  if [ $? -eq 1 ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  
  if [ "$new_password" != "$confirm" ]; then
    dialog --msgbox "Passwords do not match!" 6 40
    return
  fi
  
  new_hashed=$(echo "$new_password" | sha256sum | awk '{print $1}')
  
  # Update password in database
  sed -i "s/^$username:$old_hashed$/$username:$new_hashed/" "$db_file"
  dialog --msgbox "Password changed successfully for '$username' in $group_name!" 6 55
}

# Set Notification function (ntfy)
set_notification() {
  message=$(dialog --inputbox "Enter notification message:" 8 60 2>&1 >/dev/tty)
  if [ $? -eq 1 ] || [ -z "$message" ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  
  title=$(dialog --inputbox "Enter notification title (optional):" 8 60 2>&1 >/dev/tty)
  
  dialog --infobox "Sending notification..." 5 40
  
  if [ -n "$title" ]; then
    output=$(curl -s -d "$message" -H "Title: $title" ntfy.sh/termux_main 2>&1)
  else
    output=$(curl -s -d "$message" ntfy.sh/termux_main 2>&1)
  fi
  
  if [ $? -eq 0 ]; then
    dialog --msgbox "Notification sent successfully!\n\nTopic: termux_main\nMessage: $message" 10 60
  else
    dialog --msgbox "Failed to send notification.\n\n$output" 10 60
  fi
}

# Add Task function (Taskwarrior)
add_task() {
  if ! command -v task &>/dev/null; then
    dialog --yesno "Taskwarrior is not installed. Install it now?" 7 50
    if [ $? -eq 0 ]; then
      if [ "$ENV" = "termux" ]; then
        pkg install -y task 2>&1
      else
        $PKG_CMD install -y taskwarrior 2>&1 || sudo apt install -y taskwarrior 2>&1
      fi
    else
      return
    fi
  fi
  
  task_desc=$(dialog --inputbox "Enter task description:" 8 60 2>&1 >/dev/tty)
  if [ $? -eq 1 ] || [ -z "$task_desc" ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  
  priority=$(dialog --clear --menu "Select priority:" 12 50 3 \
    "H" "High" \
    "M" "Medium" \
    "L" "Low" \
    2>&1 >/dev/tty)
  
  if [ $? -eq 1 ]; then
    priority=""
  fi
  
  if [ -n "$priority" ]; then
    output=$(task add "$task_desc" priority:$priority 2>&1)
  else
    output=$(task add "$task_desc" 2>&1)
  fi
  
  dialog --msgbox "Task added!\n\n$output" 10 60
}

# Due Task function (Taskwarrior)
due_task() {
  if ! command -v task &>/dev/null; then
    dialog --msgbox "Taskwarrior is not installed. Please install it first." 6 55
    return
  fi
  
  # Show existing tasks
  tasks=$(task list 2>&1)
  dialog --title "Current Tasks" --msgbox "$tasks" 20 70
  
  task_id=$(dialog --inputbox "Enter task ID to set due date:" 8 50 2>&1 >/dev/tty)
  if [ $? -eq 1 ] || [ -z "$task_id" ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  
  # Get date input
  year=$(dialog --inputbox "Enter year (YYYY):" 8 40 "$(date +%Y)" 2>&1 >/dev/tty)
  if [ $? -eq 1 ] || [ -z "$year" ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  
  month=$(dialog --inputbox "Enter month (MM):" 8 40 "$(date +%m)" 2>&1 >/dev/tty)
  if [ $? -eq 1 ] || [ -z "$month" ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  
  day=$(dialog --inputbox "Enter day (DD):" 8 40 "$(date +%d)" 2>&1 >/dev/tty)
  if [ $? -eq 1 ] || [ -z "$day" ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  
  # Get time input
  hour=$(dialog --inputbox "Enter hour (HH, 24-hour format):" 8 50 "12" 2>&1 >/dev/tty)
  if [ $? -eq 1 ]; then
    hour="00"
  fi
  
  minute=$(dialog --inputbox "Enter minute (MM):" 8 40 "00" 2>&1 >/dev/tty)
  if [ $? -eq 1 ]; then
    minute="00"
  fi
  
  # Taskwarrior format: YYYY-MM-DDTHH:MM:SS
  due_date="${year}-${month}-${day}T${hour}:${minute}:00"
  
  output=$(task "$task_id" modify due:"$due_date" 2>&1)
  
  dialog --msgbox "Task due date set!\n\nDue: $due_date\n\n$output" 12 60
}

# Start the main menu
main_menu
