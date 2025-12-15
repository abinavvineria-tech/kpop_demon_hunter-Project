#!/data/data/com.termux/files/usr/bin/bash

HUNTRIX_DB="users.json"
SALT="huntrix2025_secure_salt"

hash_password() {
  echo -n "$1$SALT" | openssl dgst -sha256 | cut -d' ' -f2
}

user_exists() {
  jq -r --arg user "$1" '.[] | select(.username == $user) | .username' "$HUNTRIX_DB" 2>/dev/null | grep -q "^$1$"
}

get_user_hash() {
  jq -r --arg user "$1" '.[] | select(.username == $user) | .password' "$HUNTRIX_DB" 2>/dev/null
}

add_user() {
  local username="$1" password="$2"
  local hash=$(hash_password "$password")

  if user_exists "$username"; then
    echo "❌ User '$username' already exists!"
    return 1
  fi

  jq ". += [{\"username\":\"$username\",\"password\":\"$hash\"}]" "$HUNTRIX_DB" >tmp.json && mv tmp.json "$HUNTRIX_DB"
  echo "✅ User '$username' created successfully!"
}

validate_login() {
  local username="$1" password="$2"
  local stored_hash=$(get_user_hash "$username")

  if [[ -z "$stored_hash" ]]; then
    echo "❌ User not found!"
    return 1
  fi

  local input_hash=$(hash_password "$password")
  if [[ "$stored_hash" == "$input_hash" ]]; then
    echo "✅ Login successful! Welcome $username"
    export HUNTRIX_USER="$username"
    return 0
  else
    echo "❌ Invalid password!"
    return 1
  fi
}

change_password() {
  if [[ -z "$HUNTRIX_USER" ]]; then
    echo "❌ Must be logged in to change password!"
    return 1
  fi

  echo "Enter current password:"
  read -s current_pass
  echo

  if ! validate_login "$HUNTRIX_USER" "$current_pass"; then
    return 1
  fi

  echo "Enter new password:"
  read -s new_pass1
  echo "Confirm new password:"
  read -s new_pass2
  echo

  if [[ "$new_pass1" != "$new_pass2" ]]; then
    echo "❌ Passwords don't match!"
    return 1
  fi

  if [[ ${#new_pass1} -lt 6 ]]; then
    echo "❌ Password must be at least 6 characters!"
    return 1
  fi

  local new_hash=$(hash_password "$new_pass1")
  jq --arg user "$HUNTRIX_USER" --arg hash "$new_hash" \
    'map(if .username == $user then .password = $hash else . end)' \
    "$HUNTRIX_DB" >tmp.json && mv tmp.json "$HUNTRIX_DB"

  echo "✅ Password changed successfully for $HUNTRIX_USER!"
}

show_menu() {
  clear
  echo "🔥 HUNTRIX MULTI-TOOL v1.0 🔥"
  echo "================================"
  echo "1. 🔐 Sign In"
  echo "2. ➕ Sign Up"
  echo "3. 🔄 Change Password"
  echo "4. 🚪 Logout"
  echo "5. ❌ Exit"
  echo "================================"
  echo -n "Choose option: "
}

main_menu() {
  while true; do
    show_menu
    read -r choice

    case $choice in
    1)
      echo "Enter username:"
      read username
      echo "Enter password:"
      read -s password
      echo
      validate_login "$username" "$password" || continue
      echo "Press Enter to continue..."
      read
      ;;
    2)
      echo "Enter username:"
      read username
      echo "Enter password:"
      read -s password
      echo
      if [[ ${#password} -lt 6 ]]; then
        echo "❌ Password must be at least 6 characters!"
        sleep 2
        continue
      fi
      add_user "$username" "$password" || continue
      sleep 2
      ;;
    3)
      change_password || sleep 2
      ;;
    4)
      unset HUNTRIX_USER
      echo "👋 Logged out!"
      sleep 1
      ;;
    5)
      echo "👋 Goodbye!"
      exit 0
      ;;
    *)
      echo "❌ Invalid option!"
      sleep 1
      ;;
    esac
  done
}

# Initialize database if missing
[[ ! -f "$HUNTRIX_DB" ]] && echo '[]' >"$HUNTRIX_DB"

main_menu
