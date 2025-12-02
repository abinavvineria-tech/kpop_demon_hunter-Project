#!/data/data/com.termux/files/usr/bin/bash

# Typing Test using dialog in Termux/Bash
# Save as typing_test.sh, then: chmod +x typing_test.sh && ./typing_test.sh

dialog --backtitle "Typing Test" --clear --title " Welcome " \
  --msgbox "Test your typing speed!\n\nType the shown text exactly.\nPress OK to start." 10 40

# Generate random text (50 chars of mixed letters)
TEXT=$(cat /dev/urandom | tr -dc 'a-zA-Z ' | fold -w50 | head -n1 | sed 's/ //g')

# Show text to type with input box below
CHOICE=$(dialog --backtitle "Typing Test" --clear --title " Type this: $TEXT " \
  --inputbox "Enter the text above:\n\nResult will show WPM & accuracy." 12 60 "$TEXT" \
  3>&1 1>&2 2>&3)

EXIT_CODE=$?

clear

if [ $EXIT_CODE -eq 0 ]; then
  # Calculate metrics
  CORRECT_CHAR=$(echo -n "$TEXT" | grep -o . | paste -sd '' | wc -c)
  TYPED_CHAR=$(echo -n "$CHOICE" | wc -c)
  MATCH_CHAR=$(echo -n "$CHOICE" | grep -o "$TEXT" | wc -c)
  ACCURACY=$((MATCH_CHAR * 100 / CORRECT_CHAR))
  WPM=$((TYPED_CHAR * 60 / 30)) # Assume ~30s test

  dialog --backtitle "Typing Test" --title " Results " \
    --msgbox "Text: $TEXT\n\nYour input: $CHOICE\n\nCharacters: $TYPED_CHAR/$CORRECT_CHAR\nAccuracy: $ACCURACY%\nWords per minute: ~$WPM WPM" \
    14 60

  dialog --title " Play Again? " --yesno "Try another test?" 8 30
  if [ $? -eq 0 ]; then
    exec "$0" # Restart script
  fi
else
  dialog --title " Cancelled " --msgbox "Typing test cancelled." 6 30
fi

clear
echo "Thanks for playing!"
