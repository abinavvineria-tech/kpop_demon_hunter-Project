#!/bin/bash

# Ensure dialog is installed
if ! command -v dialog &>/dev/null; then
  echo "dialog is not installed. Installing..."
  sudo apt install -y dialog
fi

# Main menu function
main_menu() {
  while true; do
    choice=$(dialog --clear --backtitle "Huntrix Multi-Tool" \
      --title "Main Menu" \
      --menu "Choose an option:" 15 50 6 \
      1 "Sign In" \
      2 "Sign Up" \
      3 "Change Password" \
      4 "Install Tools" \
      5 "Update System" \
      6 "Upgrade System" \
      2>&1 >/dev/tty)

    # Check if user pressed Cancel
    if [ $? -eq 1 ]; then
      dialog --msgbox "Exiting..." 6 40
      exit 0
    fi

    case $choice in
    1) sign_in ;;
    2) sign_up ;;
    3) change_password ;;
    4) install_tools ;;
    5) update_system ;;
    6) upgrade_system ;;
    *) exit 0 ;;
    esac
  done
}

# Sign In function
sign_in() {
  username=$(dialog --inputbox "Enter username:" 8 40 2>&1 >/dev/tty)
  if [ $? -eq 1 ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  password=$(dialog --insecure --passwordbox "Enter password:" 8 40 2>&1 >/dev/tty)
  if [ $? -eq 1 ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  dialog --msgbox "Signing in as $username..." 6 40
}

# Sign Up function
sign_up() {
  username=$(dialog --inputbox "Enter new username:" 8 40 2>&1 >/dev/tty)
  if [ $? -eq 1 ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  password=$(dialog --insecure --passwordbox "Enter password:" 8 40 2>&1 >/dev/tty)
  if [ $? -eq 1 ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  confirm=$(dialog --insecure --passwordbox "Confirm password:" 8 40 2>&1 >/dev/tty)
  if [ $? -eq 1 ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  if [ "$password" = "$confirm" ]; then
    dialog --msgbox "Account created for $username!" 6 40
  else
    dialog --msgbox "Passwords do not match!" 6 40
  fi
}

# Change Password function
change_password() {
  username=$(dialog --inputbox "Enter username:" 8 40 2>&1 >/dev/tty)
  if [ $? -eq 1 ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  old_password=$(dialog --insecure --passwordbox "Enter old password:" 8 40 2>&1 >/dev/tty)
  if [ $? -eq 1 ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  new_password=$(dialog --insecure --passwordbox "Enter new password:" 8 40 2>&1 >/dev/tty)
  if [ $? -eq 1 ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  confirm=$(dialog --insecure --passwordbox "Confirm new password:" 8 40 2>&1 >/dev/tty)
  if [ $? -eq 1 ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  if [ "$new_password" = "$confirm" ]; then
    dialog --msgbox "Password changed for $username!" 6 40
  else
    dialog --msgbox "Passwords do not match!" 6 40
  fi
}

# Install Tools function
install_tools() {
  tool=$(dialog --inputbox "Enter tool name to install:" 8 40 2>&1 >/dev/tty)
  if [ $? -eq 1 ]; then
    dialog --msgbox "Cancelled." 6 40
    return
  fi
  sudo apt install -y "$tool"
  dialog --msgbox "$tool installed successfully!" 6 40
}

# Update System function
update_system() {
  sudo apt update
  dialog --msgbox "System updated!" 6 40
}

# Upgrade System function
upgrade_system() {
  sudo apt upgrade -y
  dialog --msgbox "System upgraded!" 6 40
}

# Start the main menu
main_menu
