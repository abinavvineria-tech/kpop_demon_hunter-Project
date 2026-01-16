import time
import random
import os
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich.progress import track
from rich.align import Align
from rich.live import Live

console = Console()
DATA_FILE = "huntrix_stats.txt"

# --- Utility Functions ---
def save_log(activity, hunter, score, rank):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {activity} | {hunter} | Score: {score} | Rank: {rank}\n")

def get_huntrix_blessing():
    members = ["Rumi", "Mira", "Zoey"]
    member = random.choice(members)
    multiplier = round(random.uniform(1.1, 1.8), 2)
    return member, multiplier

# --- Module 1: Aura Trainer ---
def aura_trainer(hunter):
    console.print("\n[bold magenta]✦ AURA CALIBRATION STARTING ✦[/bold magenta]")
    # Aura combines hidden luck + current focus
    focus = IntPrompt.ask("Concentration Level (1-100)", default=50)
    
    for _ in track(range(5), description="Extracting Soul Aura..."):
        time.sleep(0.3)
    
    base_aura = random.randint(100, 500) + (focus * 2)
    member, mult = get_huntrix_blessing()
    total_aura = int(base_aura * mult)
    
    rank = "S-CLASS" if total_aura > 800 else "A-CLASS" if total_aura > 500 else "TRAINEE"
    
    res = Panel(f"Hunter: {hunter}\nBlessing: {member} ({mult}x)\n[bold yellow]Total Aura: {total_aura}[/bold yellow]\nRank: {rank}", title="AURA RESULT", border_style="magenta")
    console.print(res)
    save_log("Aura Training", hunter, total_aura, rank)

# --- Module 2: Luck Trainer ---
def luck_trainer(hunter):
    console.print("\n[bold yellow]🎲 DESTINY ALIGNMENT (Luck Training)[/bold yellow]")
    console.print("Try to stop the pulse at the right time...")
    time.sleep(1)
    
    # Simple luck game: rolling 3 '7's
    rolls = [random.randint(1, 7) for _ in range(3)]
    console.print(f"Your Fate Crystals: [bold cyan]{rolls}[/bold cyan]")
    
    luck_score = sum(rolls) * 10
    rank = "GODLY LUCK" if 7 in rolls and sum(rolls) > 15 else "UNLUCKY"
    
    console.print(Panel(f"Luck Points: {luck_score}\nOutcome: {rank}", border_style="yellow"))
    save_log("Luck Training", hunter, luck_score, rank)

# --- Module 3: Coding Trainer (Python) ---
def coding_trainer(hunter):
    console.print("\n[bold blue]🐍 PYTHON SYNTAX CHALLENGE[/bold blue]")
    questions = [
        {"q": "Keyword to import a library?", "a": "import"},
        {"q": "Data type for 'True' or 'False'?", "a": "bool"},
        {"q": "Function to display text?", "a": "print"}
    ]
    
    score = 0
    for item in questions:
        user_a = Prompt.ask(item["q"]).lower().strip()
        if user_a == item["a"]:
            console.print("[green]Correct![/green]")
            score += 100
        else:
            console.print(f"[red]Wrong! It was {item['a']}[/red]")
            
    rank = "PRO CODER" if score == 300 else "JUNIOR"
    console.print(Panel(f"Coding XP: {score}\nRank: {rank}", border_style="blue"))
    save_log("Coding Training", hunter, score, rank)

# --- Module 4: Luck Increaser ---
def luck_increaser(hunter):
    console.print("\n[bold green]✨ HUNTRIX LUCK OVERDRIVE ✨[/bold green]")
    member = Prompt.ask("Who are you training with?", choices=["Rumi", "Mira", "Zoey"])
    
    with console.status(f"[bold green]Absorbing {member}'s energy...", spinner="bouncingBall"):
        time.sleep(3)
        increase = random.randint(5, 25)
    
    console.print(f"[bold gold1]Success![/bold gold1] Your base luck has increased by [bold]+{increase}%[/bold]")
    save_log("Luck Increaser", hunter, f"+{increase}%", member)

# --- Main Menu ---
def main():
    console.clear()
    console.print(Align.center("[bold white on magenta]  HUNTRIX TRAINING COMMAND CENTER  [/bold white on magenta]"))
    
    hunter_name = Prompt.ask("\nEnter your Hunter Name")
    
    while True:
        menu = Table.grid(expand=True)
        menu.add_column(justify="center")
        menu.add_row(Panel("[1] Aura Trainer\n[2] Luck Trainer\n[3] Coding Trainer (Python)\n[4] Luck Increaser\n[5] View History\n[0] Exit", title="SELECT MODULE", border_style="cyan"))
        
        console.print(menu)
        choice = Prompt.ask("Action", choices=["1", "2", "3", "4", "5", "0"])

        if choice == "1": aura_trainer(hunter_name)
        elif choice == "2": luck_trainer(hunter_name)
        elif choice == "3": coding_trainer(hunter_name)
        elif choice == "4": luck_increaser(hunter_name)
        elif choice == "5":
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, "r") as f: print(f.read())
            else: print("No history found.")
        elif choice == "0":
            console.print("[bold red]Shutting down. Stay safe, Hunter.[/bold red]")
            break
        
        input("\nPress Enter to return to menu...")
        console.clear()

if __name__ == "__main__":
    main()

