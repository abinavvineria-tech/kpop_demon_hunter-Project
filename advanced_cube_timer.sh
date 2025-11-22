#!/bin/bash

TIMES_FILE="cube_times.txt"
OLL_FILE="oll_cases.txt"
PLL_FILE="pll_cases.txt"
EMAIL="abimavvineria@gmail.com"
SUBJECT="Cube Timer Alert"
TMP_SCRAMBLE="../../usr/tmp/scrambles.txt"

# Basic 3x3 scramble generator (18 moves WCA style)
generate_scramble() {
  MOVES=(R R' R2 L L' L2 U U' U2 D D' D2 F F' F2 B B' B2)
  LAST=""
  SCRAMBLE=""
  for i in {1..20}; do
    while :; do
      MOVE=${MOVES[$RANDOM % ${#MOVES[@]}]}
      # avoid move on same face twice in a row
      [[ ${MOVE:0:1} != ${LAST:0:1} ]] && break
    done
    SCRAMBLE+="$MOVE "
    LAST=$MOVE
  done
  echo "$SCRAMBLE" >$TMP_SCRAMBLE
}

# OLL and PLL examples
load_oll_pll() {
  # Basic sample OLL and PLL cases, add more for real use
  echo -e "OLL1: R U2 R2 F R F' U2 R' F R F'\nOLL2: F R U R' U' F'" >$OLL_FILE
  echo -e "PLL1: R U' R U R U R U' R' U' R2\nPLL2: x R' U R' D2 R U' R' D2 R2 x'" >$PLL_FILE
}

send_email_alert() {
  local message=$1
  echo "$message" | msmtp --subject="$SUBJECT" "$EMAIL"
  # You should configure msmtp or other mail client with Gmail SMTP beforehand.
}

show_timer() {
  SECONDS=0
  while true; do
    TIME_FORMAT=$(date -u -d @${SECONDS} +%M:%S.%2N 2>/dev/null || date -u -r $SECONDS +%M:%S.%2N)
    dialog --title "Cube Timer Running" --no-shadow --infobox "Time: $TIME_FORMAT\n\nPress Ctrl+C to stop timer" 7 30
    sleep 0.1
  done
}

main_menu() {
  while true; do
    generate_scramble
    SCRAMBLE=$(cat $TMP_SCRAMBLE)
    CHOICE=$(dialog --clear --title "Cube Timer" --menu "Scramble:\n$SCRAMBLE\nSelect an option:" 15 50 8 \
      1 "Start Solve (15s inspection)" \
      2 "Show OLL Trainer" \
      3 "Show PLL Trainer" \
      4 "Show Saved Times" \
      5 "Exit" 3>&1 1>&2 2>&3)

    clear
    case $CHOICE in
    1)
      # Inspection countdown
      for i in {15..1}; do
        dialog --title "Inspection Countdown" --infobox "Inspect: $i seconds remaining..." 5 30
        sleep 1
      done

      # Start timer
      START_TIME=$(date +%s.%N)
      dialog --clear --title "Timer Running" --msgbox "Press OK to stop timer" 5 30 &
      TIMER_PID=$!

      trap "kill $TIMER_PID; end_solve $START_TIME" SIGINT SIGTERM
      wait $TIMER_PID
      trap - SIGINT SIGTERM
      end_solve $START_TIME
      ;;

    2)
      dialog --title "OLL Trainer" --msgbox "$(cat $OLL_FILE)" 20 50
      ;;

    3)
      dialog --title "PLL Trainer" --msgbox "$(cat $PLL_FILE)" 20 50
      ;;

    4)
      if [[ -f $TIMES_FILE ]]; then
        dialog --title "Saved Times" --msgbox "$(cat $TIMES_FILE)" 20 50
      else
        dialog --title "Saved Times" --msgbox "No times saved yet." 5 30
      fi
      ;;

    5)
      clear
      exit 0
      ;;

    *)
      continue
      ;;
    esac
  done
}

end_solve() {
  local start=$1
  local end=$(date +%s.%N)
  local elapsed=$(echo "$end - $start" | bc)
  local elapsed_fmt=$(printf "%.2f" $elapsed)
  dialog --title "Solve Complete" --msgbox "Time: $elapsed_fmt seconds" 6 30

  # Save time with scramble
  echo "$(date '+%Y-%m-%d %H:%M:%S') | $elapsed_fmt sec | Scramble: $(cat $TMP_SCRAMBLE)" >>$TIMES_FILE

  # Send email alert
  send_email_alert "New Cube solve time: $elapsed_fmt seconds with scramble:\n$(cat $TMP_SCRAMBLE)"

  dialog --msgbox "Time saved and email alert sent." 6 40
}

# Initialization
load_oll_pll
main_menu
