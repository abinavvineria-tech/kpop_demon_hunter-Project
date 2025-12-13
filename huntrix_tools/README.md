# Huntrix Tools

A collection of command-line tools and games themed around the "Huntrix" K-Pop Demon Hunter group.

## Contents

### 🎮 Games & Entertainment

*   **`huntrix_game.py`**: A guessing game where you test your knowledge about Huntrix members (Rumi, Mira, Zoey). Features high score tracking (`huntrix_scores.json`).
*   **`huntrix_char.py`**: Character profile viewer/generator.
*   **`huntrix_introduction.txt`**: Detailed lore and background information about the group and their demon-hunting activities.

### 🛠️ Utilities

*   **`huntrix_multi_tool_v3.sh`**: The latest version of the interactive terminal user interface (TUI) tool.
    *   **Features**:
        *   System updates (Termux/Linux)
        *   User registration/signup simulation
        *   Password management
        *   Taskwarrior integration (Add tasks, set due dates)
        *   Package installation helper
    *   **Requirements**: `dialog`, `taskwarrior`

*   **`huntrix_mc.sh` / `huntrix_mc_v2.sh`**: Shell scripts for managing Huntrix-themed mission control or tasks.

## Usage

To run the tools, ensure you have Python 3 and Bash installed.

```bash
# Run the game
python3 huntrix_game.py

# Launch the Multi-Tool
bash huntrix_multi_tool_v3.sh
```

## Requirements

*   Python 3.x
*   Bash
*   `dialog` (for shell scripts)
*   `taskwarrior` (for task management features)
