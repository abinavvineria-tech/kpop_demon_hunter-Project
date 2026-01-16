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

# --- CONFIGURATION ---
SECRET_KEY = "huntrix2026"

def save_log(path, activity, hunter, score, rank, trainer):
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"[{timestamp}] {activity} | Hunter: {hunter} | Trainer: {trainer} | Score: {score} | Rank: {rank}\n"
    try:
        with open(path, "a", encoding="utf-8") as f:
            f.write(entry)
    except Exception as e:
        console.print(f"[red]Write Error: {e}[/red]")

# --- Core Modules ---

def aura_trainer(hunter, path):
    # Select the Huntrix member for this session
    members = ["Rumi", "Mira", "Zoey"]
    trainer = random.choice(members)
    
    console.print(f"\n[bold magenta]✨ {trainer} is stepping into the training circle with you...[/bold magenta]")
    focus = IntPrompt.ask(f"[cyan]Focus your energy (1-100)[/cyan]", default=50)
    
    # Visual simulation of training
    for _ in track(range(10), description=f"[magenta]Resonating with {trainer}'s Aura...[/magenta]"):
        time.sleep(0.1)
    
    # Calculation
    base_aura = random.randint(300, 700)
    multiplier = 1.5 if focus > 80 else 1.0
    total_score = int(base_aura * multiplier)
    
    rank = "S-TIER" if total_score > 900 else "A-TIER" if total_score > 600 else "B-TIER"
    
    # Display Result
    result_panel = Panel(
        Align.center(
            f"Hunter: [bold white]{hunter}[/bold white]\n"
            f"Mentor: [bold magenta]{trainer}[/bold magenta]\n\n"
            f"AURA POWER: [bold yellow]{total_score}[/bold yellow]\n"
            f"RANK: {rank}"
        ),
        title="TRAINING COMPLETE",
        border_style="magenta"
    )
    console.print(result_panel)
    save_log(path, "Aura Training", hunter, total_score, rank, trainer)

def luck_trainer(hunter, path):
    trainer = random.choice(["Rumi", "Mira", "Zoey"])
    console.print(f"\n[bold yellow]🎲 {trainer} is testing your destiny...[/bold yellow]")
    time.sleep(1)
    
    luck_val = random.randint(1, 1000)
    rank = "DIVINE" if luck_val > 800 else "LUCKY" if luck_val > 500 else "COMMON"
    
    console.print(Panel(f"LUCK SCORE: {luck_val}\nRANK: {rank}", border_style="yellow"))
    save_log(path, "Luck Training", hunter, luck_val, rank, trainer)

def python_trainer(hunter, path):
    trainer = "Zoey" # Zoey is often portrayed as the tech-savvy one
    console.print(f"\n[bold blue]🐍 {trainer}'s Python Logic Gate[/bold blue]")
    
    q = "Which function returns the length of a list?"
    ans = Prompt.ask(q, choices=["len", "count", "size"], default="len")
    
    score = 100 if ans == "len" else 0
    rank = "MASTER" if score == 100 else "NOVICE"
    
    console.print(f"[bold green]Verified.[/bold green]" if score == 100 else "[bold red]Failed.[/bold red]")
    save_log(path, "Python Code", hunter, score, rank, trainer)

# --- Main App ---

def main():
    # Password Check
    console.clear()
    console.print(Panel.fit("[bold magenta]HUNTRIX SECURE TERMINAL[/bold magenta]", border_style="magenta"))
    attempt = getpass.getpass("PASSWORD: ")
    if attempt != SECRET_KEY:
        console.print("[red]ACCESS DENIED.[/red]")
        return

    # Setup
    save_path = Prompt.ask("Log file path", default="huntrix_logs.txt")
    hunter_name = Prompt.ask("Hunter Codename")

    while True:
        console.clear()
        console.print(Align.center("[bold white on magenta] HUNTRIX COMMAND CENTER [/bold white on magenta]"))
        
        menu = Table.grid(expand=True)
        menu.add_row(Panel(
            "[1] Aura Trainer (w/ Members)\n"
            "[2] Luck Trainer\n"
            "[3] Python Trainer\n"
            "[4] View History\n"
            "[0] Logout", 
            title="SELECT MODULE", border_style="cyan"
        ))
        console.print(menu)
        
        choice = Prompt.ask("Action", choices=["1", "2", "3", "4", "0"])

        if choice == "1": aura_trainer(hunter_name, save_path)
        elif choice == "2": luck_trainer(hunter_name, save_path)
        elif choice == "3": python_trainer(hunter_name, save_path)
        elif choice == "4":
            if os.path.exists(save_path):
                with open(save_path, "r") as f: 
                    console.print(Panel(f.read(), title="MISSION HISTORY", border_style="white"))
            else:
                console.print("[red]No logs found.[/red]")
        elif choice == "0":
            console.print("[bold magenta]Disconnecting... Happy Hunting![/bold magenta]")
            break
        
        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Session Aborted.[/red]")

