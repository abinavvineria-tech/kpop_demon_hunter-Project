#!/bin/bash

# Check for dialog, install if missing
if ! command -v dialog &> /dev/null; then
    pkg install dialog -y
fi

# Huntrix registration prompts
name=$(dialog --inputbox "Enter your name for Huntrix registration:" 8 50 3>&1 1>&2 2>&3 3>&-)
age=$(dialog --inputbox "Enter your age:" 8 50 3>&1 1>&2 2>&3 3>&-)
email=$(dialog --inputbox "Enter your email:" 8 50 3>&1 1>&2 2>&3 3>&-)

# Add --passwordbox for password (hidden input)
password=$(dialog --passwordbox "Set your Huntrix group password:" 8 50 3>&1 1>&2 2>&3 3>&-)

# Confirm dialog, password not shown
dialog --msgbox "Registration Complete!
Name: $name
Age: $age
Email: $email
Password: [hidden]" 10 50

# Save registration info
echo "$name,$age,$email,$password" >> huntrix_registrations.csv

clear
echo "Your registration for Huntrix group is complete!"
