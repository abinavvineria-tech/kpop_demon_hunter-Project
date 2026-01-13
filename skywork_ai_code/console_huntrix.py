#!/usr/bin/env python3
"""
Console Huntrix Game
A word search game for terminal/console environments
"""

import random
import string
import os
import sys

class HuntrixConsoleGame:
    def __init__(self, size=8, words=None):
        self.size = size
        self.words = words or ["PYTHON", "CODE", "GAME", "CONSOLE", "HUNT", "WORD", "GRID", "PUZZLE"]
        self.grid = []
        self.found_words = []
        self.score = 0
        self.create_grid()
        self.place_words()
        self.fill_empty_spaces()

    def create_grid(self):
        """Create an empty grid"""
        self.grid = [[' ' for _ in range(self.size)] for _ in range(self.size)]

    def place_words(self):
        """Place words in the grid in various directions"""
        directions = [
            (0, 1),   # right
            (1, 0),   # down
            (1, 1),   # diagonal down-right
            (1, -1),  # diagonal down-left
        ]

        for word in self.words:
            placed = False
            attempts = 0
            while not placed and attempts < 100:
                direction = random.choice(directions)
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - 1)

                if self.can_place_word(word, row, col, direction):
                    self.place_word(word, row, col, direction)
                    placed = True
                attempts += 1

    def can_place_word(self, word, row, col, direction):
        """Check if a word can be placed at the given position"""
        dr, dc = direction
        for i, letter in enumerate(word):
            r, c = row + i * dr, col + i * dc
            if r < 0 or r >= self.size or c < 0 or c >= self.size:
                return False
            if self.grid[r][c] != ' ' and self.grid[r][c] != letter:
                return False
        return True

    def place_word(self, word, row, col, direction):
        """Place a word in the grid"""
        dr, dc = direction
        for i, letter in enumerate(word):
            r, c = row + i * dr, col + i * dc
            self.grid[r][c] = letter

    def fill_empty_spaces(self):
        """Fill empty spaces with random letters"""
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == ' ':
                    self.grid[i][j] = random.choice(string.ascii_uppercase)

    def display_grid(self):
        """Display the grid"""
        print("  " + " ".join([str(i) for i in range(self.size)]))
        for i, row in enumerate(self.grid):
            print(str(i) + " " + " ".join(row))

    def check_word(self, word):
        """Check if word is in the word list and not already found"""
        word = word.upper()
        if word in self.words and word not in self.found_words:
            self.found_words.append(word)
            self.score += len(word) * 10
            return True
        return False

    def game_status(self):
        """Return game status information"""
        return f"Score: {self.score} | Found: {len(self.found_words)}/{len(self.words)}"

    def show_help(self):
        """Show game instructions"""
        print("\n" + "="*50)
        print("HUNTRIX CONSOLE GAME INSTRUCTIONS:")
        print("="*50)
        print("1. Find words hidden in the letter grid")
        print("2. Words can be horizontal, vertical, or diagonal")
        print("3. Type words you find and press Enter")
        print("4. Each letter is worth 10 points")
        print("5. Find all words to win!")
        print("6. Type 'quit' to exit the game")
        print("="*50 + "\n")

def main():
    """Main game loop"""
    print("Welcome to Console Huntrix!")
    print("A word search puzzle game\n")

    # Get grid size from user
    try:
        size = input("Enter grid size (default 8): ").strip()
        size = int(size) if size else 8
        size = max(5, min(15, size))  # Limit between 5 and 15
    except ValueError:
        size = 8

    # Initialize game
    game = HuntrixConsoleGame(size=size)

    # Show help
    game.show_help()

    # Main game loop
    while len(game.found_words) < len(game.words):
        # Show grid and status
        print("\n" + game.game_status())
        print("\nGrid:")
        game.display_grid()

        # Get user input
        word = input("\nEnter a word you found (or 'quit' to exit): ").strip()

        if word.lower() == 'quit':
            print(f"\nThanks for playing! Final Score: {game.score}")
            print(f"Words found: {len(game.found_words)}/{len(game.words)}")
            return

        if not word:
            continue

        # Check word
        if game.check_word(word):
            print(f"✓ Correct! Found word: {word.upper()} (+{len(word)*10} points)")
        else:
            print(f"✗ '{word.upper()}' is not a valid word or already found.")

    # Game completed
    print("\n" + "="*50)
    print("🎉 CONGRATULATIONS! 🎉")
    print("You found all words!")
    print(f"Final Score: {game.score}")
    print("="*50)

if __name__ == "__main__":
    main()
