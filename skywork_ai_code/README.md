# Huntrix Game

A word search game with two versions:
1. Termux version using Dialog interface
2. Console version for any Python environment

## Installation

For Termux version:
1. Install dialog:
   ```
   pkg install dialog
   ```

2. Run the game:
   ```
   python huntrix.py
   ```

For Console version (works everywhere):
```
python console_huntrix.py
```

## How to Play

1. Find words hidden in the letter grid
2. Words can be horizontal, vertical, or diagonal
3. Enter words you find
4. Each letter is worth 10 points
5. Find all words to win!

## Requirements

- Python 3.x
- dialog utility for Termux version (pkg install dialog in Termux)

## Game Features

- Randomly generated word search grids
- Score tracking
- Word validation
- Two interface options:
  - Interactive dialog-based (Termux)
  - Simple console-based (Universal)
