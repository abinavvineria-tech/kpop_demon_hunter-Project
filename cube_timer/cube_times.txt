#!/bin/bash

# --- Configuration ---
# Number of moves for the 3x3x3 scramble
SCRAMBLE_LENGTH=20
# Delay for visual effect (optional, in seconds)
VISUAL_DELAY=0.1

# --- Check for Dependencies ---
if ! command -v bc &> /dev/null
then
    echo "Error: 'bc' is not installed. Please install it for floating point calculations."
    echo "On Debian/Ubuntu: sudo apt install bc"
    echo "On Fedora/CentOS: sudo yum install bc"
    exit 1
fi

# --- Helper Functions ---

# Function to clear the screen
clear_screen() {
    printf "\033c" # ANSI escape code for clear screen
}

# Function to generate a simple 3x3x3 scramble
generate_scramble() {
    local moves=("U" "D" "L" "R" "F" "B")
    local suffixes=("" "'" "2") # No suffix, prime, double
    local scramble_string=""
    local last_move_face="" # To prevent consecutive moves on the same face (e.g., U U')

    for (( i=0; i<SCRAMBLE_LENGTH; i++ )); do
        local current_face=""
        while true; do
            # Pick a random face
            current_face=${moves[$RANDOM % ${#moves[@]}]}
            # Ensure it's not the same face as the last move's face
            # This is a simplified rule; true WCA scrambles prevent moves on parallel faces too.
            if [[ "$current_face" != "$last_move_face" ]]; then
                break
            fi
        done
        
        local suffix=${suffixes[$RANDOM % ${#suffixes[@]}]}
        scramble_string+="$current_face$suffix "
        last_move_face=$current_face
    done
    echo "$scramble_string"
}

# --- Main Timer Logic ---

echo "Welcome to the Bash Cube Timer!"
echo "--------------------------------"

while true; do
    clear_screen
    echo "Generating a new scramble..."
    current_scramble=$(generate_scramble)
    echo "Scramble: $current_scramble"
    echo "--------------------------------"
    echo "Press SPACE to start the timer."
    echo "Press 'q' at any prompt to quit."

    # Wait for the start key press
    read -s -n 1 -r key # -s: silent, -n 1: 1 character, -r: raw input
    
    if [[ "$key" == "q" || "$key" == "Q" ]]; then
        break # Exit the main loop
    elif [[ "$key" == " " ]]; then
        # Timer started
        start_time=$(date +%s.%N)
        echo -e "\nTimer started! Press SPACE to stop..."

        # Wait for the stop key press
        read -s -n 1 -r key
        
        if [[ "$key" == "q" || "$key" == "Q" ]]; then
            break # Exit the main loop
        elif [[ "$key" == " " ]]; then
            end_time=$(date +%s.%N)
            
            # Calculate elapsed time using bc for floating point arithmetic
            elapsed_time=$(echo "$end_time - $start_time" | bc -l)

            clear_screen
            echo "--------------------------------"
            printf "Your time: %.2f seconds\n" "$elapsed_time"
            echo "Scramble: $current_scramble" # Show scramble with the time
            echo "--------------------------------"
            echo "Press ENTER for another solve, or 'q' to quit."
            
            read -r continue_choice # Read full line for 'q' or ENTER
            if [[ "$continue_choice" == "q" || "$continue_choice" == "Q" ]]; then
                break # Exit the main loop
            fi
        fi
    fi
done

clear_screen
echo "Exiting Cube Timer. Goodbye!"
echo "--------------------------------"
