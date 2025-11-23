#!/bin/bash

# Termux cube timer + scramble + OLL/PLL trainer script using dialog

# 3x3 scramble moves
moves=(U D L R F B)
suffixes=("" "'" "2")

# OLL cases and algs (partial set for example)
declare -A oll_cases=(
  ["OLL 1"]="R U2 R2 F R F' U2 R' F R F'"
  ["OLL 2"]="F R U' R' U' R U R' F'"
  ["OLL 3"]="r U r' U2 r U2 R' U2 R U' r'"
)

# PLL cases and algs (partial set for example)
declare -A pll_cases=(
  ["PLL Ua"]="R U' R U R U R U' R' U' R2"
  ["PLL Ub"]="R2 U R U R' U' R' U' R' U R'"
  ["PLL H"]="M2 U M2 U2 M2 U M2"
)

function generate_scramble() {
  length=20
  scramble=""
  for ((i=0; i<length; i++)); do
    move=${moves[RANDOM % ${#moves[@]}]}
    suffix=${suffixes[RANDOM % ${#suffixes[@]}]}
    scramble+="$move$suffix "
  done
  echo "$scramble"
}

function show_timer() {
  # Timer using dialog progress box, start/stop via Enter/cancel
  dialog --title "Cube Timer" --infobox "Press Enter to start timer, Cancel to stop." 7 50
  read -rsp $'Press Enter to start timer...\n'
  start_time=$(date +%s)
  
  while true; do
    now=$(date +%s)
    elapsed=$((now - start_time))
    elapsed_fmt=$(printf "%02d:%02d.%02d" $((elapsed/60)) $((elapsed%60)) $(( ( $(date +%N) / 10000000 )%100 )))
    dialog --title "Cube Timer" --infobox "Elapsed Time: $elapsed_fmt\n\nPress Cancel or Ctrl+C to stop." 7 50
    sleep 0.1
    read -t 0.1 -n 1 key
    if [[ $? != 0 ]]; then
      # no keypress, continue
      continue
    else
      break
    fi
  done
}

function oll_trainer() {
  keys=("${!oll_cases[@]}")
  case_name=${keys[RANDOM % ${#keys[@]}]}
  alg=${oll_cases[$case_name]}
  dialog --title "OLL Trainer" --msgbox "Case: $case_name\n\nAlgorithm:\n$alg" 10 50
}

function pll_trainer() {
  keys=("${!pll_cases[@]}")
  case_name=${keys[RANDOM % ${#keys[@]}]}
  alg=${pll_cases[$case_name]}
  dialog --title "PLL Trainer" --msgbox "Case: $case_name\n\nAlgorithm:\n$alg" 10 50
}

function main_menu() {
  while true; do
    choice=$(dialog --stdout --title "Cube Trainer" --menu "Choose an option:" 15 50 6 \
      1 "Start cube timer" \
      2 "Show a new scramble" \
      3 "OLL trainer" \
      4 "PLL trainer" \
      5 "Exit")
    case $choice in
      1)
        show_timer
        ;;
      2)
        scramble=$(generate_scramble)
        dialog --title "3x3 Scramble" --msgbox "$scramble" 8 50
        ;;
      3)
        oll_trainer
        ;;
      4)
        pll_trainer
        ;;
      5)
        clear
        exit 0
        ;;
      *)
        ;;
    esac
  done
}

# Check dialog installed
if ! command -v dialog &> /dev/null; then
  echo "dialog is not installed. Please install it with:"
  echo "pkg install dialog"
  exit 1
fi

clear
main_menu
