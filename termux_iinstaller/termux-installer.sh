#!/data/data/com.termux/files/usr/bin/bash

# Termux Tool Installer
# A simple menu-driven tool to install common packages

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Banner
show_banner() {
    clear
    echo -e "${CYAN}"
    echo "╔════════════════════════════════════════╗"
    echo "║      TERMUX TOOL INSTALLER             ║"
    echo "║         by Termux User                 ║"
    echo "╚════════════════════════════════════════╝"
    echo -e "${NC}"
}

# Update packages
update_packages() {
    echo -e "${YELLOW}[*] Updating package lists...${NC}"
    pkg update -y && pkg upgrade -y
    echo -e "${GREEN}[✓] Update complete!${NC}"
    sleep 2
}

# Install a single package
install_pkg() {
    local pkg_name=$1
    echo -e "${YELLOW}[*] Installing $pkg_name...${NC}"
    if pkg install -y "$pkg_name"; then
        echo -e "${GREEN}[✓] $pkg_name installed successfully!${NC}"
    else
        echo -e "${RED}[✗] Failed to install $pkg_name${NC}"
    fi
    sleep 1
}

# Development Tools
install_dev_tools() {
    show_banner
    echo -e "${BLUE}=== Development Tools ===${NC}\n"
    echo "1) Python"
    echo "2) Node.js"
    echo "3) Ruby"
    echo "4) Golang"
    echo "5) Rust"
    echo "6) Clang (C/C++)"
    echo "7) PHP"
    echo "8) Perl"
    echo "9) Install All Dev Tools"
    echo "0) Back to Main Menu"
    echo ""
    read -p "Select option: " choice
    
    case $choice in
        1) install_pkg "python" ;;
        2) install_pkg "nodejs" ;;
        3) install_pkg "ruby" ;;
        4) install_pkg "golang" ;;
        5) install_pkg "rust" ;;
        6) install_pkg "clang" ;;
        7) install_pkg "php" ;;
        8) install_pkg "perl" ;;
        9) 
            for pkg in python nodejs ruby golang rust clang php perl; do
                install_pkg "$pkg"
            done
            ;;
        0) return ;;
        *) echo -e "${RED}Invalid option${NC}"; sleep 1 ;;
    esac
    install_dev_tools
}

# Networking Tools
install_net_tools() {
    show_banner
    echo -e "${BLUE}=== Networking Tools ===${NC}\n"
    echo "1) curl"
    echo "2) wget"
    echo "3) nmap"
    echo "4) netcat"
    echo "5) openssh"
    echo "6) hydra"
    echo "7) dnsutils"
    echo "8) traceroute"
    echo "9) Install All Net Tools"
    echo "0) Back to Main Menu"
    echo ""
    read -p "Select option: " choice
    
    case $choice in
        1) install_pkg "curl" ;;
        2) install_pkg "wget" ;;
        3) install_pkg "nmap" ;;
        4) install_pkg "netcat-openbsd" ;;
        5) install_pkg "openssh" ;;
        6) install_pkg "hydra" ;;
        7) install_pkg "dnsutils" ;;
        8) install_pkg "traceroute" ;;
        9) 
            for pkg in curl wget nmap netcat-openbsd openssh hydra dnsutils traceroute; do
                install_pkg "$pkg"
            done
            ;;
        0) return ;;
        *) echo -e "${RED}Invalid option${NC}"; sleep 1 ;;
    esac
    install_net_tools
}

# Utility Tools
install_util_tools() {
    show_banner
    echo -e "${BLUE}=== Utility Tools ===${NC}\n"
    echo "1) git"
    echo "2) vim"
    echo "3) nano"
    echo "4) tmux"
    echo "5) htop"
    echo "6) zip/unzip"
    echo "7) tar"
    echo "8) ffmpeg"
    echo "9) Install All Utilities"
    echo "0) Back to Main Menu"
    echo ""
    read -p "Select option: " choice
    
    case $choice in
        1) install_pkg "git" ;;
        2) install_pkg "vim" ;;
        3) install_pkg "nano" ;;
        4) install_pkg "tmux" ;;
        5) install_pkg "htop" ;;
        6) install_pkg "zip" && install_pkg "unzip" ;;
        7) install_pkg "tar" ;;
        8) install_pkg "ffmpeg" ;;
        9) 
            for pkg in git vim nano tmux htop zip unzip tar ffmpeg; do
                install_pkg "$pkg"
            done
            ;;
        0) return ;;
        *) echo -e "${RED}Invalid option${NC}"; sleep 1 ;;
    esac
    install_util_tools
}

# Security Tools
install_sec_tools() {
    show_banner
    echo -e "${BLUE}=== Security Tools ===${NC}\n"
    echo "1) sqlmap"
    echo "2) metasploit"
    echo "3) john (password cracker)"
    echo "4) hashcat"
    echo "5) aircrack-ng"
    echo "6) termux-api"
    echo "7) tsu (root access)"
    echo "8) Install All Security Tools"
    echo "0) Back to Main Menu"
    echo ""
    read -p "Select option: " choice
    
    case $choice in
        1) install_pkg "sqlmap" ;;
        2) install_pkg "unstable-repo" && install_pkg "metasploit" ;;
        3) install_pkg "john" ;;
        4) install_pkg "hashcat" ;;
        5) install_pkg "aircrack-ng" ;;
        6) install_pkg "termux-api" ;;
        7) install_pkg "tsu" ;;
        8) 
            install_pkg "unstable-repo"
            for pkg in sqlmap metasploit john hashcat aircrack-ng termux-api tsu; do
                install_pkg "$pkg"
            done
            ;;
        0) return ;;
        *) echo -e "${RED}Invalid option${NC}"; sleep 1 ;;
    esac
    install_sec_tools
}

# Custom Package Install
custom_install() {
    show_banner
    echo -e "${BLUE}=== Custom Package Install ===${NC}\n"
    read -p "Enter package name (or 'q' to quit): " pkg_name
    if [[ "$pkg_name" != "q" && -n "$pkg_name" ]]; then
        install_pkg "$pkg_name"
        custom_install
    fi
}

# Search Package
search_package() {
    show_banner
    echo -e "${BLUE}=== Search Package ===${NC}\n"
    read -p "Enter search term: " search_term
    if [[ -n "$search_term" ]]; then
        echo -e "${YELLOW}[*] Searching for '$search_term'...${NC}\n"
        pkg search "$search_term"
        echo ""
        read -p "Press Enter to continue..."
    fi
}

# Main Menu
main_menu() {
    while true; do
        show_banner
        echo -e "${GREEN}=== MAIN MENU ===${NC}\n"
        echo "1) Update & Upgrade Packages"
        echo "2) Development Tools"
        echo "3) Networking Tools"
        echo "4) Utility Tools"
        echo "5) Security Tools"
        echo "6) Custom Package Install"
        echo "7) Search Package"
        echo "0) Exit"
        echo ""
        read -p "Select option: " choice
        
        case $choice in
            1) update_packages ;;
            2) install_dev_tools ;;
            3) install_net_tools ;;
            4) install_util_tools ;;
            5) install_sec_tools ;;
            6) custom_install ;;
            7) search_package ;;
            0) 
                echo -e "${GREEN}Goodbye!${NC}"
                exit 0
                ;;
            *) 
                echo -e "${RED}Invalid option${NC}"
                sleep 1
                ;;
        esac
    done
}

# Run
main_menu
