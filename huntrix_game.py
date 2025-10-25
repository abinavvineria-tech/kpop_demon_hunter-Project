import random
import json
import os
from datetime import datetime


def load_scores():
    """Load scores from JSON file. Create file if it doesn't exist."""
    if os.path.exists('huntrix_scores.json'):
        try:
            with open('huntrix_scores.json', 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            # If file is corrupted or empty, start fresh
            return {"high_scores": [], "game_history": []}
    else:
        return {"high_scores": [], "game_history": []}


def save_scores(scores_data):
    """Save scores to JSON file."""
    with open('huntrix_scores.json', 'w') as f:
        json.dump(scores_data, f, indent=4)


def display_high_scores(scores_data):
    """Display the top 10 high scores."""
    if not scores_data["high_scores"]:
        print("No high scores yet. Be the first!")
        return

    print("" + "="*50)
    print("🏆 HIGH SCORES (Top 10) 🏆")
    print("="*50)

    # Sort by attempts (lower is better) and take top 10
    sorted_scores = sorted(
        scores_data["high_scores"], key=lambda x: x["attempts_used"])[:10]

    for idx, score in enumerate(sorted_scores, 1):
        print(f"{idx}. {score['player_name']
                        } - {score['attempts_used']} attempts")
        print(f"   Member: {score['member']} | Date: {score['date']}")
    print("="*50)


def guessing_game():
    """
    A game where the user guesses the age of a randomly selected Huntrix member.
    Stores high scores and game history in a JSON file.
    """
    scores_data = load_scores()

    huntrix_members = {
        "Rumi": 24,
        "Mira": 23,
        "Zoey": 22,
    }

    member_name, correct_age = random.choice(list(huntrix_members.items()))

    max_attempts = 169
    attempts_used = 0
    all_guesses = []

    print(f"I'm thinking of a member of Huntrix. Can you guess her age?")
    print(f"You have {max_attempts} attempts to guess the age of... {
          member_name}!")
    print("-" * 50)

    remaining_attempts = max_attempts

    while remaining_attempts > 0:
        try:
            guess_str = input(f"Enter your guess for {member_name}'s age: ")
            guess = int(guess_str)

            attempts_used += 1
            all_guesses.append(guess)

            if guess < correct_age:
                print("Too low! Try a higher number.")
            elif guess > correct_age:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed it right!")
                print(f"{member_name} is indeed {correct_age} years old.")
                print(f"You got it in {attempts_used} attempt(s)!")

                player_name = input(
                    "Enter your name for the high score board: ").strip() or "Anonymous"

                game_record = {
                    "player_name": player_name,
                    "member": member_name,
                    "correct_age": correct_age,
                    "attempts_used": attempts_used,
                    "guesses": all_guesses,
                    "result": "win",
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

                scores_data["high_scores"].append(game_record)
                scores_data["game_history"].append(game_record)
                save_scores(scores_data)

                display_high_scores(scores_data)
                return

            remaining_attempts -= 1
            if remaining_attempts > 0:
                print(f"You have {remaining_attempts} attempts left.")

        except ValueError:
            print("Invalid input. Please enter a number.")
            print(f"You still have {remaining_attempts} attempts left.")

    print("Game over! You've run out of attempts.")
    print(f"The correct age for {member_name} was {correct_age}.")

    game_record = {
        "player_name": "N/A",
        "member": member_name,
        "correct_age": correct_age,
        "attempts_used": max_attempts,
        "guesses": all_guesses,
        "result": "loss",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    scores_data["game_history"].append(game_record)
    save_scores(scores_data)


def view_game_history(scores_data):
    """Displays the last 10 games played."""
    if not scores_data["game_history"]:
        print("No game history yet. Play a game first!")
        return

    print("" + "="*50)
    print("📊 GAME HISTORY (Last 10 Games) 📊")
    print("="*50)
    for idx, game in enumerate(scores_data["game_history"][-10:][::-1], 1):
        result_icon = "✅" if game["result"] == "win" else "❌"
        player = game['player_name'] if game['result'] == 'win' else '---'
        print(f"{idx}. {result_icon} Player: {
              player} | Member: {game['member']}")
        print(f"   Guesses: {game['guesses']} | Result: {
              game['result'].upper()}")
        print(f"   Date: {game['date']}")
    print("="*50)


def main():
    """Main function to run the game with a menu."""
    while True:
        print("" + "="*50)
        print("🎮 HUNTRIX AGE GUESSING GAME 🎮")
        print("="*50)
        print("1. Play Game")
        print("2. View High Scores")
        print("3. View Game History")
        print("4. Exit")
        print("="*50)

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            guessing_game()
        elif choice == "2":
            scores_data = load_scores()
            display_high_scores(scores_data)
        elif choice == "3":
            scores_data = load_scores()
            view_game_history(scores_data)
        elif choice == "4":
            print("Thanks for playing! Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
