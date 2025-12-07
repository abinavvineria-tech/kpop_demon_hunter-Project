#!/bin/bash
# Huntrix Multi Tool - Bash Version
# Abinav's lore edition ⚡
# Requires: dialog, taskwarrior, curl, termux-api (optional)

# Ensure dialog is installed
pkg install -y dialog

while true; do
  CHOICE=$(dialog --clear --backtitle "Huntrix Multi Tool ⚡" \
    --title "Main Menu" \
    --menu "Choose your destiny:" 20 70 10 \
    1 "Update Tool (apt update/upgrade)" \
    2 "Install Tool (pkg install)" \
    3 "Signup (Huntrix fandom)" \
    4 "Password Manager (Groups)" \
    5 "Task Manager (Taskwarrior)" \
    6 "Cube Timer (Speedcubing)" \
    7 "File Manager (ls)" \
    8 "Aura System (Lore Ritual)" \
    9 "Fandom Rituals (Huntrix)" \
    10 "Send ntfy Notification" \
    11 "Exit" \
    2>&1 >/dev/tty)

  case $CHOICE in
  1)
    apt update && apt upgrade -y
    dialog --msgbox "✅ Tool updated successfully!" 6 40
    ;;
  2)
    TOOL=$(dialog --inputbox "Enter tool to install:" 8 60 2>&1 >/dev/tty)
    pkg install -y "$TOOL"
    dialog --msgbox "✅ Installed $TOOL" 6 40
    ;;
  3)
    USER=$(dialog --inputbox "Enter username:" 8 60 2>&1 >/dev/tty)
    PASS=$(dialog --passwordbox "Enter password:" 8 60 2>&1 >/dev/tty)
    dialog --msgbox "👤 Signup complete for $USER" 6 40
    ;;
  4)
    NEW_PASS=$(dialog --passwordbox "Enter new password:" 8 60 2>&1 >/dev/tty)
    dialog --msgbox "🔒 Password updated successfully!" 6 40
    ;;
  5)
    task list || dialog --msgbox "📋 Taskwarrior not installed!" 6 40
    ;;
  6)
    dialog --msgbox "🧊 Cube Timer: Press OK to start" 6 40
    START=$(date +%s)
    dialog --msgbox "Press OK to stop" 6 40
    END=$(date +%s)
    TIME=$((END - START))
    dialog --msgbox "🧊 Cube solve time: $TIME seconds" 6 40
    ;;
  7)
    FILES=$(ls -lh)
    dialog --msgbox "📂 Files:\n$FILES" 20 70
    ;;
  8)
    dialog --msgbox "✨ Aura ritual activated! Huntrix energy flows..." 6 50
    ;;
  9)
    dialog --msgbox "🎶 Performing Huntrix fandom ritual..." 6 50
    ;;
  10)
    TOPIC=$(dialog --inputbox "Enter ntfy topic:" 8 60 2>&1 >/dev/tty)
    MSG=$(dialog --inputbox "Enter message:" 8 60 2>&1 >/dev/tty)
    curl -d "$MSG" "https://ntfy.sh/$TOPIC"
    dialog --msgbox "📢 Notification sent: $MSG" 6 50
    ;;
  11)
    clear
    echo "Exiting Huntrix Multi Tool... Goodbye ⚡"
    exit 0
    ;;
  esac
done
