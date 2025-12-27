#!/bin/bash

# Huntrix Super Multi Tool

function show_menu() {
  echo "============================"
  echo "     Huntrix Multi Tool     "
  echo "============================"
  echo "1. System Info"
  echo "2. Network Info"
  echo "3. Disk Usage"
  echo "4. Backup Directory"
  echo "5. Find Files"
  echo "6. Exit"
  echo -n "Choose an option: "
}

function system_info() {
  echo "System Information:"
  uname -a
  echo "Uptime:"
  uptime
}

function network_info() {
  echo "Network Information:"
  ip a
  echo "Current Connections:"
  ss -tuln
}

function disk_usage() {
  echo "Disk Usage:"
  df -h
}

function backup_directory() {
  echo -n "Enter the directory to backup: "
  read dir
  echo -n "Enter the destination for backup: "
  read dest
  tar -cvzf "$dest/backup_$(date +%Y%m%d).tar.gz" "$dir"
  echo "Backup completed successfully."
}

function find_files() {
  echo -n "Enter the directory to search: "
  read dir
  echo -n "Enter the filename to search for: "
  read filename
  find "$dir" -name "$filename"
}

while true; do
  show_menu
  read option
  case $option in
  1) system_info ;;
  2) network_info ;;
  3) disk_usage ;;
  4) backup_directory ;;
  5) find_files ;;
  6) exit 0 ;;
  *) echo "Invalid option. Please try again." ;;
  esac
  echo -e "\n"
done
