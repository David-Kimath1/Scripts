#!/bin/bash

# Colors
GREEN=$'\033[0;32m'
CYAN=$'\033[0;36m'
YELLOW=$'\033[1;33m'
RED=$'\033[0;31m'
RESET=$'\033[0m'

# Pause function
pause() {
    echo
    read -p "Press Enter to return to menu..."
}

# Header
header() {
    clear
    echo -e "${CYAN}==============================${RESET}"
    echo -e "${CYAN}     D4V3 SYSTEM TOOLKIT      ${RESET}"
    echo -e "${CYAN}==============================${RESET}"
    echo
}

# System Information
system_info() {
    clear
    echo -e "${CYAN}==============================${RESET}"
    echo -e "${CYAN}      SYSTEM INFORMATION      ${RESET}"
    echo -e "${CYAN}==============================${RESET}"
    echo

    echo -e "${GREEN}User:${RESET} $(whoami)"
    echo -e "${GREEN}Hostname:${RESET} $(hostname)"
    echo -e "${GREEN}Kernel:${RESET} $(uname -r)"
    echo -e "${GREEN}Architecture:${RESET} $(uname -m)"
    echo -e "${GREEN}OS:${RESET} $(lsb_release -d | cut -f2)"
    echo -e "${GREEN}Uptime:${RESET} $(uptime -p)"

    pause
}

# Hardware Information
hardware_info() {
    clear
    echo -e "${CYAN}==============================${RESET}"
    echo -e "${CYAN}      HARDWARE INFORMATION    ${RESET}"
    echo -e "${CYAN}==============================${RESET}"
    echo

    lscpu | head -15

    pause
}

# Disk Usage
disk_usage() {
    clear
    echo -e "${CYAN}==============================${RESET}"
    echo -e "${CYAN}          DISK USAGE          ${RESET}"
    echo -e "${CYAN}==============================${RESET}"
    echo

    df -h

    pause
}

# Network Information
network_info() {
    clear
    echo -e "${CYAN}==============================${RESET}"
    echo -e "${CYAN}     NETWORK INFORMATION      ${RESET}"
    echo -e "${CYAN}==============================${RESET}"
    echo

    ip addr

    pause
}

# Process Viewer
process_info() {
    clear
    echo -e "${CYAN}==============================${RESET}"
    echo -e "${CYAN}     RUNNING PROCESSES        ${RESET}"
    echo -e "${CYAN}==============================${RESET}"
    echo

    ps aux --sort=-%cpu | head -10

    pause
}


# Main Menu Loop
while true
do
    header

    echo -e "${GREEN}1.${RESET} System Information"
    echo -e "${GREEN}2.${RESET} Hardware Information"
    echo -e "${GREEN}3.${RESET} Disk Usage"
    echo -e "${GREEN}4.${RESET} Network Information"
    echo -e "${GREEN}5.${RESET} Running Processes"
    echo -e "${RED}6.${RESET} Exit"

    echo
    read -p "Choose an option: " choice

    case $choice in

    1)
        system_info
        ;;

    2)
        hardware_info
        ;;

    3)
        disk_usage
        ;;

    4)
        network_info
        ;;

    5)
        process_info
        ;;

    6)
        clear
        echo -e "${GREEN}Closing D4V3 SYSTEM TOOLKIT...${RESET}"
        sleep 1
        exit
        ;;

    *)
        echo -e "${RED}Invalid option${RESET}"
        sleep 1
        ;;

    esac

done
