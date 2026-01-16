import time
import random
import os
import getpass
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich.progress import track
from rich.align import Align

console = Console()

# --- SECURITY & LOGO ---
SECRET_KEY = "huntrix2026"

LOGO = """
[bold magenta]
  _    _ _    _ _   _ _______ _____  _______   __
 | |  | | |  | | \ | |__   __|  __ \|_   _\ \ / /
 | |__| | |  | |  \| |  | |  | |__) | | |  \ V / 
 |  __  | |  | | . ` |  | |  |  _  /  | |   > <  
 | |  | | |__| | |\  |  | |  | | \ \ _| |_ / . \ 
 |_|  |_|\____/|_| \_|  |_|  |_|  \_\_____/_/ \_\\
      ✦ K-POP DEMON HUNTER COMMAND CENTER ✦
[/bold magenta]
"""

def save_log(path, activity, hunter, score, rank, trainer):
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"[{timestamp}] {activity} | Hunter: {hunter} | Trainer: {trainer} | Score: {score} | Rank: {rank}\n"
    with open(path, "a", encoding="utf-8") as f:
        f.write(entry)

# --- THE 4 CORE TRAINING MODULES ---

def aura_trainer(hunter, path):
    trainer = random.choice(["Rumi", "Mira", "Zoey"])
    console.print(f"\n[bold magenta]✦ {trainer.upper()}'S AURA CHAMBER ✦[/bold magenta]")
    focus = IntPrompt.ask("[cyan]Focus Level (1-100)[/cyan]", default=50)
    for _ in track(range(10), description="Harmonizing..."):
        time.sleep(0.1)
    score = int(random.randint(400, 800) * (1.5 if focus > 85 else 1.0))
    rank = "S-CLASS" if score > 900 else "A-CLASS"
    console.print(Panel(f"MENTOR: {trainer}\nAURA: {score}\nRANK: {rank}", border_style="magenta"))
    save_log(path, "Aura", hunter, score, rank, trainer)

def luck_trainer(hunter, path):
    trainer = random.choice(["Rumi", "Mira", "Zoey"])
    console.print(f"\n[bold yellow]🎲 {trainer.upper()}'S DESTINY ROLL 🎲[/bold yellow]")
    with console.status("[yellow]Spinning Fate...", spinner="point"):
        time.sleep(1.5)
        luck = random.randint(1, 1000)
    rank = "DIVINE" if luck > 900 else "LUCKY"
    console.print(Panel(f"LUCK: {luck}\nRANK: {rank}", border_style="yellow"))
    save_log(path, "Luck", hunter, luck, rank, trainer)

def coding_trainer(hunter, path):
    trainer = "Zoey"
    console.print(f"\n[bold blue]🐍 {trainer.upper()}'S PYTHON TEST[/bold blue]")
    q = random.choice([{"q": "Indent with?", "a": "spaces"}, {"q": "List symbol?", "a": "[]"}])
    ans = Prompt.ask(q["q"]).lower()
    score, rank = (100, "PASS") if ans == q["a"] else (0, "FAIL")
    console.print(f"[bold {'green' if score else 'red'}]{rank}[/bold {'green' if score else 'red'}]")
    save_log(path, "Python", hunter, score, rank, trainer)

def luck_increaser(hunter, path):
    trainer = random.choice(["Rumi", "Mira", "Zoey"])
    console.print(f"\n[bold green]✨ {trainer.upper()}'S OVERDRIVE ✨[/bold green]")
    for _ in track(range(15), description="Infusing..."):
        time.sleep(0.05)
    boost = f"+{random.randint(10, 50)}%"
    console.print(f"[gold1]Luck Boosted: {boost}[/gold1]")
    save_log(path, "Boost", hunter, boost, "ACTIVE", trainer)

# --- SYSTEM MAIN ---

def main():
    console.clear()
    console.print(LOGO)
    pw = getpass.getpass("SYSTEM ACCESS KEY: ")
    if pw != SECRET_KEY:
        console.print("[red]ACCESS DENIED.[/red]")
        return

    save_path = Prompt.ask("\nSet Save File", default="huntrix_logs.txt")
    hunter_name = Prompt.ask("Hunter Name")

    while True:
        console.clear()
        console.print(Align.center(LOGO))
        console.print(f"[grey]Hunter: {hunter_name} | Logs: {save_path}[/grey]\n")
        
        menu = Table.grid(expand=True)
        menu.add_row(Panel(
            "[1] Aura Trainer\n[2] Luck Trainer\n[3] Python Lab\n[4] Luck Overdrive\n[5] View History\n[0] Logout", 
            title="CORE SYSTEM", border_style="cyan"
        ))
        console.print(menu)
        
        choice = Prompt.ask("Action", choices=["1", "2", "3", "4", "5", "0"])

        if choice == "1": aura_trainer(hunter_name, save_path)
        elif choice == "2": luck_trainer(hunter_name, save_path)
        elif choice == "3": coding_trainer(hunter_name, save_path)
        elif choice == "4": luck_increaser(hunter_name, save_path)
        elif choice == "5":
            if os.path.exists(save_path):
                with open(save_path, "r") as f: console.print(Panel(f.read(), title="LOGS"))
            else: console.print("[red]No history found.[/red]")
        elif choice == "0": break
        input("\n[Enter] to Return...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Session Aborted.[/red]")

