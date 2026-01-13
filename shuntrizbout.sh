#!/bin/bash

# Check if dialog is installed
if ! command -v dialog &> /dev/null
then
    echo "Dialog is not installed. Please install it using:"
    echo "pkg install dialog"
    exit 1
fi

# Main menu function
main_menu() {
    CHOICE=$(dialog --clear --no-lines --backtitle "Huntrix - K-Pop Demon Hunters" \
        --title "Main Menu" \
        --menu "Welcome to the Huntrix Information Center!\n\nUse arrow keys to navigate and Enter to select." 15 70 5 \
        1 "Group Profile" \
        2 "Members" \
        3 "Discography" \
        4 "Mission History" \
        5 "Exit" \
        3>&1 1>&2 2>&3)

    EXIT_STATUS=$?

    # Handle Cancel/ESC
    if [ $EXIT_STATUS -ne 0 ]; then
        exit_program
    fi

    case $CHOICE in
        1) group_profile ;;
        2) members ;;
        3) discography ;;
        4) mission_history ;;
        5) exit_program ;;
        *) main_menu ;;
    esac
}

# Group Profile Section
group_profile() {
    dialog --backtitle "Huntrix - Group Profile" \
        --title "About Huntrix" \
        --msgbox "Huntrix is a unique K-pop group formed by celestial decree to protect the Earth from supernatural threats.\n\nFormed: 2023\nGenre: Dark Pop/Supernatural Fusion\nAgency: Celestial Entertainment\nMission: Protect humanity from demonic incursions while delivering chart-topping hits.\n\nKnown for their electrifying performances and supernatural battles, Huntrix has redefined what it means to be a K-pop idol in the modern age." 15 70
    main_menu
}

# Members Section
members() {
    MEMBER_CHOICE=$(dialog --clear --no-lines --backtitle "Huntrix - Members" \
        --title "Group Members" \
        --menu "Select a member to learn more:\n\nEach member possesses unique abilities that contribute to both their musical talent and demon hunting prowess." 18 70 6 \
        1 "Alex Moon - Leader/Vocalist" \
        2 "Jin Shadows - Lead Rapper" \
        3 "Riley Dawn - Lead Dancer" \
        4 "Sam Nightfall - Visual/Maknae" \
        5 "Back to Main Menu" \
        3>&1 1>&2 2>&3)

    EXIT_STATUS=$?

    # Handle Cancel/ESC
    if [ $EXIT_STATUS -ne 0 ]; then
        main_menu
    fi

    case $MEMBER_CHOICE in
        1) alex_moon ;;
        2) jin_shadows ;;
        3) riley_dawn ;;
        4) sam_nightfall ;;
        5) main_menu ;;
        *) members ;;
    esac
}

# Individual Member Profiles
alex_moon() {
    dialog --backtitle "Member Profile - Alex Moon" \
        --title "Alex Moon - Leader & Main Vocalist" \
        --msgbox "Real Name: Alexander Kim\nAge: 23\nPosition: Leader, Main Vocalist\nAbilities: Light Manipulation, Divine Protection\nSignature Move: Solar Flare Harmony\n\nAlex was chosen as leader due to his natural charisma and powerful light-based abilities that counteract dark forces. His vocals can purify corrupted areas and weaken demonic entities." 15 70
    members
}

jin_shadows() {
    dialog --backtitle "Member Profile - Jin Shadows" \
        --title "Jin Shadows - Lead Rapper" \
        --msgbox "Real Name: Park Jin Woo\nAge: 21\nPosition: Lead Rapper\nAbilities: Shadow Step, Fear Immunity\nSignature Move: Phantom Rhymes\n\nJin's mastery over shadows allows him to scout enemy positions and move undetected during missions. His rap verses can disorient and confuse demonic opponents." 15 70
    members
}

riley_dawn() {
    dialog --backtitle "Member Profile - Riley Dawn" \
        --title "Riley Dawn - Lead Dancer" \
        --msgbox "Real Name: Riley Nakamura\nAge: 20\nPosition: Lead Dancer, Sub Vocalist\nAbilities: Time Dilation, Enhanced Reflexes\nSignature Move: Temporal Spin\n\nRiley's temporal manipulation powers make her invaluable in combat situations, allowing her to slow down opponents. Her dance moves can create temporal rifts that trap enemies." 15 70
    members
}

sam_nightfall() {
    dialog --backtitle "Member Profile - Sam Nightfall" \
        --title "Sam Nightfall - Visual/Maknae" \
        --msgbox "Real Name: Samuel Rodriguez\nAge: 19\nPosition: Visual, Maknae, Lead Vocalist\nAbilities: Dream Walking, Illusion Casting\nSignature Move: Nightmare Serenade\n\nAs the youngest member, Sam's illusion abilities are crucial for reconnaissance and psychological warfare against demons. His vocals can induce prophetic dreams in allies." 15 70
    members
}

# Discography Section
discography() {
    dialog --backtitle "Huntrix - Discography" \
        --title "Music Releases" \
        --msgbox "Albums:\n1. 'Darkness Before Dawn' (2023) - Debut Album\n   - Hit single: 'Demon's Cry'\n   - Chart position: #1 for 4 weeks\n\n2. 'Eclipse' (2024) - First Full-Length Album\n   - Hit single: 'Shadow Dance'\n   - Chart position: #1 for 6 weeks\n\n3. 'Midnight Crusaders' (2025) - Latest Release\n   - Hit single: 'Hunter's Anthem'\n   - Current chart position: #1\n\nTotal Sales: 2.3 Million Copies\nAwards: 15 Major Music Awards" 20 70
    main_menu
}

# Mission History Section
mission_history() {
    MISSION_CHOICE=$(dialog --clear --no-lines --backtitle "Huntrix - Mission History" \
        --title "Notable Missions" \
        --menu "Select a mission to view details:\n\nThe following are classified missions successfully completed by Huntrix." 16 70 5 \
        1 "Operation Midnight Sun" \
        2 "Project Eclipse" \
        3 "Operation Soulfire" \
        4 "Back to Main Menu" \
        3>&1 1>&2 2>&3)

    EXIT_STATUS=$?

    # Handle Cancel/ESC
    if [ $EXIT_STATUS -ne 0 ]; then
        main_menu
    fi

    case $MISSION_CHOICE in
        1) operation_midnight ;;
        2) project_eclipse ;;
        3) operation_soulfire ;;
        4) main_menu ;;
        *) mission_history ;;
    esac
}

operation_midnight() {
    dialog --backtitle "Mission Details - Operation Midnight Sun" \
        --title "Operation Midnight Sun (2023)" \
        --msgbox "Target: Class-S Demonic Incursion\nLocation: Seoul, South Korea\nOutcome: Success\nCasualties: None\n\nHuntrix's first major mission involved eliminating a powerful demon attempting to open a permanent portal to the underworld. The mission coincided with their debut performance, cleverly masking combat as choreography." 15 70
    mission_history
}

project_eclipse() {
    dialog --backtitle "Mission Details - Project Eclipse" \
        --title "Project Eclipse (2024)" \
        --msgbox "Target: Demon Cult Infiltration\nLocation: Tokyo, Japan\nOutcome: Success\nCasualties: Minor injuries to Jin Shadows\n\nA cult had been summoning lesser demons across Japan. Huntrix worked with local authorities to dismantle the organization. Their concert at Tokyo Dome served as cover for the final confrontation." 15 70
    mission_history
}

operation_soulfire() {
    dialog --backtitle "Mission Details - Operation Soulfire" \
        --title "Operation Soulfire (2025)" \
        --msgbox "Target: Archdemon Threat\nLocation: Los Angeles, USA\nOutcome: Success\nCasualties: None\n\nHuntrix's most challenging mission to date involved stopping an archdemon attempting to corrupt the city's water supply. Their performance at the Grammy Awards served as both cover and a way to reach maximum population for protection through music." 15 70
    mission_history
}

# Exit Program
exit_program() {
    dialog --backtitle "Huntrix - Goodbye" \
        --title "Exiting" \
        --msgbox "Thank you for visiting the Huntrix Information Center!\n\nStay tuned for our upcoming releases and missions.\n\n'The darkness cannot extinguish our light!' - Huntrix motto" 12 70
    clear
    echo "Thank you for using the Huntrix Information Center!"
    echo "Follow us on all social media platforms @HuntrixOfficial"
    exit 0
}

# Display welcome message
echo "Welcome to the Huntrix Information Center!"
echo "Starting the interactive menu..."

# Start the program
main_menu
