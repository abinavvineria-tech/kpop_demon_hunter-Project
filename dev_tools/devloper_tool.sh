#!/bin/bash

# Check if dialog is installed, install if missing
if ! command -v dialog &>/dev/null; then
  echo "Dialog is not installed. Installing dialog..."
  pkg install dialog -y
fi

function show_menu() {
  # Main menu
  dialog --clear --backtitle "Advanced Termux Installer" \
    --title "Main Menu" \
    --menu "Choose an installation option:" 15 50 4 \
    1 "Update packages" \
    2 "Install Basic Tools" \
    3 "Install Developer Tools" \
    4 "Exit" 2>menu_choice.txt
}

function update_packages() {
  clear
  echo "Updating packages..."
  pkg update && pkg upgrade -y
  echo "Update completed. Press any key to continue..."
  read -n 1
}

function install_basic_tools() {
  clear
  echo "Installing basic tools: git, curl, wget, nano..."
  pkg install git curl wget nano -y
  echo "Basic tools installed. Press any key to continue..."
  read -n 1
}

function install_developer_tools() {
  clear
  echo "Installing developer tools: python, nodejs, clang, make..."
  pkg install python nodejs clang make -y
  echo "Developer tools installed. Press any key to continue..."
  read -n 1
}

while true; do
  show_menu
  menuitem=$(<menu_choice.txt)
  case $menuitem in
  1) update_packages ;;
  2) install_basic_tools ;;
  3) install_developer_tools ;;
  4)
    clear
    exit 0
    ;;
  *)
    clear
    echo "Invalid option."
    sleep 2
    ;;
  esac
done
