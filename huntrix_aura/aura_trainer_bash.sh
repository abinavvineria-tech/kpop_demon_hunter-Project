#!/data/data/com.termux/files/usr/bin/bash

AURA=0
BLESS=0.5 # bless count

add_funk() {
  AURA=$((AURA + 5000)) # 10000 * 0.5
}

add_song() {
  AURA=$((AURA + 60000)) # 120000 * 0.5
}

add_mythical() {
  AURA=$((AURA + 65000)) # 130000 * 0.5
}

while true; do
  CHOICE=$(dialog --stdout \
    --title "Huntrix Aura Trainer" \
    --menu "Aura: $AURA  | Bless: $BLESS" 15 60 6 \
    1 "Listen to funk (+10,000 base)" \
    2 "Listen to their song (+120,000 base)" \
    3 "Mythical aura combo (+130,000 base)" \
    4 "Reset aura" \
    0 "Exit")

  case "$CHOICE" in
  1) add_funk ;;
  2) add_song ;;
  3) add_mythical ;;
  4) AURA=0 ;;
  0)
    clear
    exit 0
    ;;
  *) ;;
  esac
done
