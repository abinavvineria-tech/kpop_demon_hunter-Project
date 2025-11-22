import time
import random
import os

# List of moves for 3x3 scramble
moves = ["U", "D", "L", "R", "F", "B"]
suffixes = ["", "'", "2"]


def generate_scramble(length=20):
    scramble = []
    last_move = ''
    for _ in range(length):
        move = random.choice(moves)
        while move == last_move:
            move = random.choice(moves)
        last_move = move
        scramble.append(move + random.choice(suffixes))
    return ' '.join(scramble)


def timer():
    input("Press Enter to show scramble and start inspection...")
    scramble = generate_scramble()
    print(f"Scramble:\n{scramble}")
    input("Press Enter to start timer...")
    start_time = time.time()
    input("Press Enter to stop timer...")
    end_time = time.time()
    solve_time = end_time - start_time
    print(f"Solve time: {solve_time:.2f} seconds")
    with open("solve_times.txt", "a") as f:
        f.write(f"{scramble} | {solve_time:.2f} sec\n")


if __name__ == "__main__":
    print("Cube Timer for Termux")
    print("=====================")
    while True:
        timer()
        again = input("New solve? (y/n): ").strip().lower()
        if again != 'y':
            break
    print("Solve times saved in solve_times.txt")
