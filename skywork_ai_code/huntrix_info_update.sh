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
    CHOICE=$(dialog --clear --no-lines --backtitle "HUNTRIX - K-Pop Demon Hunters" \
        --title "Main Menu" \
        --menu "Welcome to the HUNTRIX Information Center!\n\nUse arrow keys to navigate and Enter to select." 16 70 6 \
        1 "Group Profile" \
        2 "Members" \
        3 "Discography" \
        4 "Songs" \
        5 "Mission History" \
        6 "Exit" \
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
        4) songs ;;
        5) mission_history ;;
        6) exit_program ;;
        *) main_menu ;;
    esac
}

# Group Profile Section
group_profile() {
    dialog --backtitle "HUNTRIX - Group Profile" \
        --title "About HUNTRIX" \
        --msgbox "HUNTRIX is a fictional three-member girl group created for the Netflix animated film 'KPop Demon Hunters'.\n\nFounded: April 24, 2025 (as a fictional group)\nDebut: June 20, 2025 - Release of K-Pop Demon Hunters\nGenre: Dark Pop/Supernatural Fusion\nAgency: Celestial Entertainment (fictional)\n\nWhile publicly recognized as K-pop idols, they secretly operate as demon hunters. They use their music to reinforce the Honmoon and prevent demons from entering the human world.\n\nThe group consists of Rumi, Mira, and Zoey." 17 70
    main_menu
}

# Members Section
members() {
    MEMBER_CHOICE=$(dialog --clear --no-lines --backtitle "HUNTRIX - Members" \
        --title "Group Members" \
        --menu "Select a member to learn more:\n\nEach member possesses unique abilities that contribute to both their musical talent and demon hunting prowess." 16 70 5 \
        1 "Rumi - Leader/Main Vocalist" \
        2 "Mira - Visual/Sub Vocalist" \
        3 "Zoey - Lead Rapper/Maknae" \
        4 "Back to Main Menu" \
        3>&1 1>&2 2>&3)

    EXIT_STATUS=$?

    # Handle Cancel/ESC
    if [ $EXIT_STATUS -ne 0 ]; then
        main_menu
    fi

    case $MEMBER_CHOICE in
        1) rumi ;;
        2) mira ;;
        3) zoey ;;
        4) main_menu ;;
        *) members ;;
    esac
}

# Individual Member Profiles
rumi() {
    dialog --backtitle "Member Profile - Rumi" \
        --title "Rumi - Leader & Main Vocalist" \
        --msgbox "Real Name: Rumi\nAge: 23-24\nPosition: Leader, Main Vocalist\nAbilities: Half demon/half human heritage, Light Manipulation, Divine Protection\nSignature Move: Solar Flare Harmony\n\nRumi is the charismatic leader of HUNTRIX. She is a cambion—half demon and half human—born to a famous K-pop idol mother who also fought demons. Her powerful vocals can purify corrupted areas and weaken demonic entities. Her voice actor is Arden Cho, with EJAE providing her singing voice." 17 70
    members
}

mira() {
    dialog --backtitle "Member Profile - Mira" \
        --title "Mira - Visual/Sub Vocalist" \
        --msgbox "Real Name: Mira\nAge: 23-24\nPosition: Visual, Sub Vocalist\nAbilities: Dream Walking, Illusion Casting\nSignature Move: Nightmare Serenade\n\nMira's illusion abilities are crucial for reconnaissance and psychological warfare against demons. Her vocals can induce prophetic dreams in allies to prepare them for upcoming battles. She was born in Seoul, South Korea. Her voice actor is May Hong, with Audrey Nuna providing her singing voice." 16 70
    members
}

zoey() {
    dialog --backtitle "Member Profile - Zoey" \
        --title "Zoey - Lead Rapper/Maknae" \
        --msgbox "Real Name: Zoey\nAge: 22-23\nPosition: Lead Rapper, Maknae (youngest member)\nAbilities: Lyricist, Sonic Illusions\nSignature Move: Beat Drop Banishment\n\nZoey is the lyricist of HUNTRIX and the youngest member (maknae). She was born in Los Angeles, California, USA. Her rap skills and ability to create sonic illusions can confuse and disorient demons. She also serves as the group's lead rapper. Her voice actor is Ji-young Yoo, with Rei Ami providing her singing voice." 16 70
    members
}

# Discography Section
discography() {
    dialog --backtitle "HUNTRIX - Discography" \
        --title "Music Releases" \
        --msgbox "Soundtrack from 'KPop Demon Hunters' (2025):\n\nFeatured Songs:\n- 'Golden'\n- 'How It's Done'\n- 'What It Sounds Like'\n- 'Takedown'\n- 'Free'\n\nThe soundtrack was released on June 20, 2025, through Republic Records and features nine original songs written by Danny Chung. It reached #1 on multiple music charts and sold over 1.8 million copies worldwide.\n\nEach member has two vocal performers: one for speaking voice and one for singing voice." 18 70
    main_menu
}

# Songs Section
songs() {
    SONG_CHOICE=$(dialog --clear --no-lines --backtitle "HUNTRIX - Songs" \
        --title "HUNTRIX Songs" \
        --menu "Select a song to learn more:\n\nEach song has special meaning in the HUNTRIX universe." 16 70 5 \
        1 "Golden" \
        2 "How It's Done" \
        3 "What It Sounds Like" \
        4 "Back to Main Menu" \
        3>&1 1>&2 2>&3)

    EXIT_STATUS=$?

    # Handle Cancel/ESC
    if [ $EXIT_STATUS -ne 0 ]; then
        main_menu
    fi

    case $SONG_CHOICE in
        1) golden ;;
        2) how_its_done ;;
        3) what_it_sounds_like ;;
        4) main_menu ;;
        *) songs ;;
    esac
}

golden() {
    dialog --backtitle "HUNTRIX - Golden" \
        --title "Golden" \
        --msgbox "Song: Golden\n\n'Golden' is one of HUNTRIX's most popular tracks from the KPop Demon Hunters soundtrack.\n\nWhat it sounds like:\n- An energetic K-pop anthem with powerful vocals\n- Features a catchy beat with electronic elements\n- Incorporates both Rumi's soaring vocals and Zoey's rap verses\n- Has an uplifting melody that contrasts with the dark themes of the movie\n- Became a viral hit with over 100M streams on various platforms\n\nThe song represents the group's determination to shine despite the darkness they face." 17 70
    songs
}

how_its_done() {
    dialog --backtitle "HUNTRIX - How It's Done" \
        --title "How It's Done" \
        --msgbox "Song: How It's Done\n\n'How It's Done' is one of HUNTRIX's signature tracks from the KPop Demon Hunters soundtrack.\n\nWhat it sounds like:\n- A dynamic track that showcases each member's unique talents\n- Features Mira's melodic vocals, Rumi's powerful range, and Zoey's rap skills\n- Incorporates electronic and hip-hop elements\n- Has a confident, empowering message about proving yourself\n- Became popular for its choreography and catchy hook\n\nThe song plays during key action sequences in the film and represents the group's growth as both performers and demon hunters." 17 70
    songs
}

what_it_sounds_like() {
    dialog --backtitle "HUNTRIX - What It Sounds Like" \
        --title "What It Sounds Like" \
        --msgbox "Song: What It Sounds Like\n\n'What It Sounds Like' is HUNTRIX's emotional climax song performed at Namsan Tower in the film.\n\nWhat it sounds like:\n- An emotional ballad that builds to an empowering anthem\n- Features all three members' vocals in harmony\n- Incorporates orchestral elements with electronic production\n- Has heartfelt lyrics about unity and finding your voice\n- Features a powerful key change in the final chorus\n- Became a fan favorite for its emotional resonance\n\nIn the film, this song represents the trio's reunion after their trials and their combined power to fight the main demon threat. It's when they finally perform the song they couldn't write earlier in the story." 18 70
    songs
}

# Mission History Section
mission_history() {
    MISSION_CHOICE=$(dialog --clear --no-lines --backtitle "HUNTRIX - Mission History" \
        --title "Notable Missions" \
        --menu "Select a mission to view details:\n\nThe following are key events from the KPop Demon Hunters storyline." 14 70 4 \
        1 "Main Storyline" \
        2 "Confrontation with Saja Boys" \
        3 "Back to Main Menu" \
        3>&1 1>&2 2>&3)

    EXIT_STATUS=$?

    # Handle Cancel/ESC
    if [ $EXIT_STATUS -ne 0 ]; then
        main_menu
    fi

    case $MISSION_CHOICE in
        1) main_storyline ;;
        2) saja_boys ;;
        3) main_menu ;;
        *) mission_history ;;
    esac
}

main_storyline() {
    dialog --backtitle "Mission Details - Main Storyline" \
        --title "KPop Demon Hunters Main Storyline" \
        --msgbox "In the film, Rumi, Mira, and Zoey work to protect the world from demons and hope to accomplish that through their music.\n\nKey plot points:\n- Rumi's bandmates (Mira and Zoey) are temporarily replaced with imposter demons\n- Rumi's demon marks are revealed on stage against her will\n- She is humiliated and faces challenges to her identity\n- The trio must work together to defeat the main demon threat\n- They use their music as a weapon against supernatural forces\n\nThe film explores themes of identity, acceptance, and the power of music." 18 70
    mission_history
}

saja_boys() {
    dialog --backtitle "Mission Details - Saja Boys Confrontation" \
        --title "Confrontation with Saja Boys" \
        --title "Confrontation with Saja Boys" \
        --msgbox "HUNTRIX faces off against a rival boy band, the Saja Boys, whose members are secretly demons.\n\nKey details:\n- The Saja Boys serve as the main antagonists\n- They attempt to corrupt the K-pop industry\n- Each member of Saja Boys is voiced by a K-pop star\n- Ahn Hyo-seop provides the voice for the main antagonist\n\nThe climactic battle takes place during a major performance, with HUNTRIX using their music to fight the demonic threat while maintaining their cover as K-pop idols." 16 70
    mission_history
}

# Exit Program
exit_program() {
    dialog --backtitle "HUNTRIX - Goodbye" \
        --title "Exiting" \
        --msgbox "Thank you for visiting the HUNTRIX Information Center!\n\nStay tuned for potential future releases.\n\n'The darkness cannot extinguish our light!' - HUNTRIX motto" 12 70
    clear
    echo "Thank you for using the HUNTRIX Information Center!"
    echo "Follow us on all social media platforms @HUNTRIXOfficial"
    exit 0
}

# Display welcome message
echo "Welcome to the HUNTRIX Information Center!"
echo "Starting the interactive menu..."

# Start the program
main_menu
