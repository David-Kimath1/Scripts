#!/bin/bash

# Colors
GREEN=$'\033[0;32m'
CYAN=$'\033[0;36m'
YELLOW=$'\033[1;33m'
RESET=$'\033[0m'

clear

# Typing effect function
type_text() {
    text="$1"
    delay="${2:-0.03}"

    for ((i=0; i<${#text}; i++)); do
        echo -n "${text:$i:1}"
        sleep "$delay"
    done

    echo
}

echo -e "${CYAN}==============================${RESET}"
type_text " Linux System Scanner" 0.05
echo -e "${CYAN}==============================${RESET}"
echo

type_text "${YELLOW}Initializing scanner...${RESET}" 0.04

echo

# Loading percentage
for i in {0..100}; do
    printf "\r${GREEN}Loading: %3d%%${RESET}" "$i"
    sleep 0.02
done

echo
echo

echo -e "${CYAN}==============================${RESET}"
type_text " Linux System Information" 0.05
echo -e "${CYAN}==============================${RESET}"
echo

# Animated result with typing
show_result() {
    echo -ne "${GREEN}[✓]${RESET} "
    
    text="$1"
    for ((i=0; i<${#text}; i++)); do
        echo -n "${text:$i:1}"
        sleep 0.04
    done
    
    echo
    sleep 0.5
}

show_result "User: $(whoami)"
show_result "Hostname: $(hostname)"
show_result "Kernel: $(uname -r)"
show_result "Architecture: $(uname -m)"
show_result "Current directory: $(pwd)"
show_result "Date: $(date)"

echo
type_text "Scan complete!" 0.05
