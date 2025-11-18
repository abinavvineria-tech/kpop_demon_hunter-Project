#!/bin/bash

while true; do
  # Show input box to get package name
  PACKAGE=$(dialog --inputbox "Enter the package name to install (or leave empty to exit):" 8 50 3>&1 1>&2 2>&3 3>&-)

  # Exit if no input
  if [ -z "$PACKAGE" ]; then
    clear
    echo "Exiting installer."
    exit 0
  fi

  # Confirm installation
  dialog --yesno "Install package: $PACKAGE?" 7 40
  RESPONSE=$?

  if [ $RESPONSE -eq 0 ]; then
    clear
    echo "Installing $PACKAGE ..."
    pkg install -y "$PACKAGE"
    echo "Press Enter to continue..."
    read
  else
    dialog --msgbox "Installation cancelled." 5 30
  fi
done
