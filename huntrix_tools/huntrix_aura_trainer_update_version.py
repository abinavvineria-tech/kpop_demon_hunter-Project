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

def ensure_directory(file_path):
    """Ensures the folder for the save path exists."""
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        try:
            os.makedirs(directory)
            console.print(f"[grey]Created directory: {directory}[/grey]")
        except Exception as e:
            console.print(f"[red]Error creating directory: {e}[/red]")

def save_log(path, activity, hunter, score, rank):
    ensure_directory(path)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"[{timestamp}] {activity} | {hunter} | Score: {score} | Rank: {rank}\n"
    try:
        with open(path, "a", encoding="utf-8") as f:
            f.write(entry)
    except Exception as e:
        console.print(f"[red]Write Error: {e}[/red]")

def check_password():
    console.clear()
    console.print(Panel.fit("[bold magenta]HUNTRIX ENCRYPTED TERMINAL[/bold magenta]", border_style="magenta"))
    # Note: getpass may not show a prompt in some IDEs; type blindly and press enter
    attempt = getpass.getpass("ID CARD REQUIRED (PASSWORD): ")
    if attempt == SECRET_KEY:
        console.print("[bold green]AUTHENTICATION SUCCESSFUL.[/bold green]\n")
        time.sleep(1)
        return True
    return False

# --- Core Modules ---
def aura_trainer(hunter, path):
    focus = IntPrompt.ask("\n[bold cyan]Channel Focus (1-100)[/bold cyan]", default=50)
    for _ in track(range(10), description="[magenta]Scanning Aura Field...[/magenta]"):
        time.sleep(0.1)
    
    score = random.randint(200, 600) + (focus * 3)
    rank = "S-TIER" if score > 800 else "A-TIER" if score > 500 else "B-TIER"
    
    console.print(Panel(f"HUNTER: {hunter}\nRESULT: {score}\nRANK: {rank}", title="AURA SCAN COMPLETE", border_style="magenta"))
    save_log(path, "Aura", hunter, score, rank)

def luck_trainer(hunter, path):
    console.print("\n[bold yellow]Rolling Fate Crystals...[/bold yellow]")
    time.sleep(1)
    luck_val = random.randint(1, 777)
    rank = "DIVINE" if luck_val > 700 else "COMMON"
    console.print(Panel(f"LUCK SCORE: {luck_val}\nRANK: {rank}", border_style="yellow"))
    save_log(path, "Luck", hunter, luck_val, rank)

def python_trainer(hunter, path):
    console.print("\n[bold blue]Python Logic Gate:[/bold blue]")
    ans = Prompt.ask("What is the keyword to exit a loop prematurely?", choices=["stop", "break", "exit"])
    score = 100 if ans == "break" else 0
    rank = "CERTIFIED" if score == 100 else "FAILED"
    console.print(f"Result: {rank}")
    save_log(path, "Python", hunter, score, rank)

# --- Main App ---
def main():
    if not check_password():
        console.print("[bold red]ACCESS DENIED. LOCKING SYSTEM.[/bold red]")
        return

    save_path = Prompt.ask("Define Log Path (e.g., /sdcard/huntrix.txt or huntrix.txt)", default="huntrix_stats.txt")
    hunter_name = Prompt.ask("Enter Hunter Name")

    while True:
        console.clear()
        console.print(Align.center("[bold white on magenta] HUNTRIX COMMAND CENTER [/bold white on magenta]"))
        
        menu = Table.grid(expand=True)
        menu.add_row(Panel("[1] Aura Trainer\n[2] Luck Trainer\n[3] Python Trainer\n[4] System Logs\n[0] Logout", title="MENU", border_style="cyan"))
        console.print(menu)
        
        choice = Prompt.ask("Action", choices=["1", "2", "3", "4", "0"])

        if choice == "1": aura_trainer(hunter_name, save_path)
        elif choice == "2": luck_trainer(hunter_name, save_path)
        elif choice == "3": python_trainer(hunter_name, save_path)
        elif choice == "4":
            if os.path.exists(save_path):
                with open(save_path, "r") as f: console.print(Panel(f.read(), title="HISTORY"))
            else: console.print("[red]No logs found.[/red]")
        elif choice == "0":
            console.print("[bold magenta]Logging out... Stream 'Golden' on your way out![/bold magenta]")
            break
        
        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()

