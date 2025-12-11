#!/bin/bash

# --- Function to generate a simple scramble ---
generate_scramble() {
  local moves=("R" "R'" "R2" "L" "L'" "L2" "U" "U'" "U2" "D" "D'" "D2" "F" "F'" "F2" "B" "B'" "B2")
  local scramble=""
  local length=20 # Standard scramble length for 3x3

  for i in $(seq 1 $length); do
    # Pick a random move
    move_index=$((RANDOM % ${#moves[@]}))
    scramble+="${moves[$move_index]} "
  done
  echo "$scramble"
}

# --- Main Timer Logic ---
timer() {
  # Clear the screen for a cleaner look
  clear

  # 1. Generate and display the scramble
  SCRAMBLE=$(generate_scramble)
  echo "================================================="
  echo "            CUBE TIMER - READY TO GO!"
  echo "================================================="
  echo "SCRAMBLE (20 moves):"
  echo -e "   \033[1m$SCRAMBLE\033[0m" # Bold the scramble
  echo "-------------------------------------------------"

  # 2. START PROMPT
  echo -e "Press \033[32mENTER\033[0m to \033[1mSTART\033[0m..."

  # Wait for the first ENTER press to start the timer
  read -r

  # Record the START time in milliseconds
  # %s is seconds since epoch, %N is nanoseconds. We convert to milliseconds.
  START_TIME=$(date +%s%3N)

  # Display the running status
  echo -e "\n\033[33mTIMER RUNNING... (Press ENTER to STOP)\033[0m"

  # 3. STOP PROMPT
  # Wait for the second ENTER press to stop the timer
  read -r

  # Record the STOP time in milliseconds
  STOP_TIME=$(date +%s%3N)

  # 4. CALCULATE ELAPSED TIME
  ELAPSED_MS=$((STOP_TIME - START_TIME))

  # Convert milliseconds to minutes, seconds, and remaining milliseconds
  TOTAL_SECONDS=$((ELAPSED_MS / 1000))
  MINUTES=$((TOTAL_SECONDS / 60))
  SECONDS=$((TOTAL_SECONDS % 60))
  MILLISECONDS=$((ELAPSED_MS % 1000))

  # 5. DISPLAY RESULT

  # Format the time (pad with leading zeros for seconds and milliseconds)
  # Note: Bash string formatting with printf is used for padding
  FORMATTED_TIME=$(printf "%d:%02d.%03d" $MINUTES $SECONDS $MILLISECONDS)

  echo -e "\n================================================="
  echo -e "\033[1;36mSOLVE TIME:\033[0m \033[1;35m$FORMATTED_TIME\033[0m"
  echo "================================================="
  echo "Press ENTER to run a new timer, or Ctrl+C to exit."
  read -r # Wait for user to acknowledge before restarting
}

# --- Loop to keep the timer running until the user stops it (Ctrl+C) ---
while true; do
  timer
done
