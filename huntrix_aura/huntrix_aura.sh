#!/bin/bash
# Huntrix Aura Ritual Script
# Abinav's aura summoning tool in Termux using dialog

# Ensure dialog is installed
command -v dialog >/dev/null 2>&1 || {
  echo "dialog not found. Install it with: pkg install dialog"
  exit 1
}

while true; do
  CHOICE=$(dialog --clear --backtitle "Huntrix Aura Ritual" \
    --title "Summon Aura" \
    --menu "Choose your aura to summon:" 15 50 6 \
    1 "🔥 Inferno Aura - Power & Rage" \
    2 "❄️ Frost Aura - Calm & Precision" \
    3 "⚡ Storm Aura - Speed & Energy" \
    4 "🌌 Void Aura - Mystery & Darkness" \
    5 "🌟 Celestial Aura - Light & Hope" \
    6 "Exit Ritual" \
    2>&1 >/dev/tty)

  clear
  case $CHOICE in
  1)
    echo "🔥 You have summoned the Inferno Aura!"
    echo "Your cube burns with Huntrix’s fiery rage..."
    ;;
  2)
    echo "❄️ You have summoned the Frost Aura!"
    echo "Your mind sharpens, times become precise..."
    ;;
  3)
    echo "⚡ You have summoned the Storm Aura!"
    echo "Speed surges through your hands, Huntrix guides your moves..."
    ;;
  4)
    echo "🌌 You have summoned the Void Aura!"
    echo "Darkness surrounds you, hidden power awakens..."
    ;;
  5)
    echo "🌟 You have summoned the Celestial Aura!"
    echo "Light fills your spirit, Huntrix blesses your ritual..."
    ;;
  6)
    echo "Exiting Huntrix Aura Ritual. Until next summon..."
    break
    ;;
  esac
  read -p "Press Enter to return to the ritual menu..."
done
