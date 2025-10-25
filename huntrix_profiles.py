#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A simple script for Termux to display profiles for the members of
# HUNTR/X from the movie "K-Pop: Demon Hunters".

# --- ANSI Color Codes for Terminal Output ---
class Colors:
    RESET = '\u001B[0m'
    BOLD = '\u001B[1m'
    CYAN = '\u001B[96m'
    PURPLE = '\u001B[95m'
    PINK = '\u001B[95m'  # Using magenta for pink
    GREEN = '\u001B[92m'
    YELLOW = '\u001B[93m'
    WHITE = '\u001B[97m'
    HEADER = '\u001B[95m'
    TITLE = '\u001B[93m'


# Data for the Huntrix members, based on available fan profiles.
# Sources: kprofiles.com, kpopdemon.com
HUNTRIX_MEMBERS = [
    {
        "name": "Rumi (루미)",
        "color": Colors.PURPLE,
        "position": "Leader, Main Vocalist, Center",
        "age": 23,
        "ability": "Spirit Magic & Sonic Resonance",
        "weapon": "Saingeom (Divine Sword)",
        "facts": [
            "Half-demon and half-human.",
            "Her voice can create and strengthen the Honmoon barrier.",
            "Voiced by Arden Cho."
        ]
    },
    {
        "name": "Mira (미라)",
        "color": Colors.PINK,
        "position": "Main Dancer, Vocalist, Choreographer",
        "age": 23,
        "ability": "Spear Combat & Hand-to-Hand Combat",
        "weapon": "Woldo (Korean Halberd)",
        "facts": [
            "Known for her elite combat and choreography skills.",
            "Left her wealthy family to become an idol.",
            "Voiced by May Hong."
        ]
    },
    {
        "name": "Zoey (조이)",
        "color": Colors.GREEN,
        "position": "Main Rapper, Lyricist, Maknae (Youngest)",
        "age": 22,
        "ability": "Knife Combat & Acrobatic Skills",
        "weapon": "Twin Sinkal Blades (Shamanic Knives)",
        "facts": [
            "Korean-American, raised in Burbank, California.",
            "Uses her creative mind and rap skills to build the group's image.",
            "Voiced by Jiyoung Yoo."
        ]
    }
]


def display_profiles():
    """Formats and prints the member profiles to the terminal."""

    print(f"{Colors.HEADER}{
          Colors.BOLD}===== HUNTR/X Member Profiles ====={Colors.RESET}")

    for member in HUNTRIX_MEMBERS:
        color = member['color']

        print(f"{color}{Colors.BOLD}◆ {member['name']}{Colors.RESET}")
        print(f"  ├─ {Colors.TITLE}Position:{Colors.RESET} {
              Colors.WHITE}{member['position']}{Colors.RESET}")
        print(f"  ├─ {Colors.TITLE}Age:{Colors.RESET}      {
              Colors.WHITE}{member['age']}{Colors.RESET}")
        print(f"  ├─ {Colors.TITLE}Ability:{Colors.RESET}  {
              Colors.WHITE}{member['ability']}{Colors.RESET}")
        print(f"  └─ {Colors.TITLE}Weapon:{Colors.RESET}   {
              Colors.WHITE}{member['weapon']}{Colors.RESET}")

        print(f"{Colors.CYAN}Key Facts:{Colors.RESET}")
        for fact in member['facts']:
            print(f"    - {Colors.WHITE}{fact}{Colors.RESET}")

        print("" + "-"*35 + "")


if __name__ == "__main__":
    display_profiles()
