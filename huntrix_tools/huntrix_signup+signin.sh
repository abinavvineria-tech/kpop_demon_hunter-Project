#!/data/data/com.termux/files/usr/bin/bash

USERDB="$HOME/.huntrix_users"

show_menu() {
  dialog --clear --title "Huntrix Group" \
    --menu "Welcome! Choose an option:" 13 50 2 \
    1 "Sign Up (Register)" \
    2 "Sign In (Login)" 2>menuitem.txt
}

signup() {
  dialog --inputbox "Enter your Huntrix username:" 8 40 2>uname.txt
  uname=$(cat uname.txt)

  dialog --passwordbox "Enter your Huntrix password:" 8 40 2>upass.txt
  upass=$(cat upass.txt)

  if grep -q "^$uname:" "$USERDB" 2>/dev/null; then
    dialog --msgbox "Username already exists. Please choose another." 6 40
    return
  fi

  echo "$uname:$(echo $upass | sha256sum | awk '{print $1}')" >>"$USERDB"
  dialog --msgbox "Registration successful for '$uname'!" 6 40
}

signin() {
  dialog --inputbox "Enter your Huntrix username:" 8 40 2>uname.txt
  uname=$(cat uname.txt)

  dialog --passwordbox "Enter your Huntrix password:" 8 40 2>upass.txt
  upass=$(cat upass.txt)

  hashed=$(echo $upass | sha256sum | awk '{print $1}')

  if grep -q "^$uname:$hashed$" "$USERDB" 2>/dev/null; then
    dialog --msgbox "Sign in successful! Welcome, $uname to Huntrix group." 6 40
  else
    dialog --msgbox "Login failed. Invalid username or password." 6 40
  fi
}

while true; do
  show_menu
  opt=$(cat menuitem.txt)
  case "$opt" in
  1) signup ;;
  2) signin ;;
  *)
    clear
    exit
    ;;
  esac
done
