from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
import random
import json
import os

console = Console()

# ===============================
# PRE-ADDED MEMBERS
# ===============================
members = {
    "Rumi":   {"aura": 50, "luck": 30, "power": 40, "level": 2, "xp": 120},
    "Mira":   {"aura": 40, "luck": 50, "power": 35, "level": 2, "xp": 130},
    "Zoey":   {"aura": 45, "luck": 40, "power": 45, "level": 2, "xp": 140},
    "Abinav": {"aura": 35, "luck": 35, "power": 30, "level": 1, "xp": 50}
}

# ===============================
# UTIL
# ===============================
def select_member():
    if not members:
        console.print("[red]⚠ No members found![/red]")
        return None
    name = Prompt.ask("[cyan]Enter member name[/cyan]")
    if name not in members:
        console.print("[red]❌ Member not found![/red]")
        return None
    return name

def gain_xp(name, amount):
    members[name]["xp"] += amount
    new_level = members[name]["xp"] // 100 + 1
    if new_level > members[name]["level"]:
        members[name]["level"] = new_level
        console.print(f"[bold green]🧬 {name} leveled up! Level {new_level}[/bold green]")

# ===============================
# CORE FEATURES
# ===============================
def add_member():
    name = Prompt.ask("[cyan]Enter new member name[/cyan]")
    if name in members:
        console.print("[red]❌ Member already exists![/red]")
        return
    members[name] = {"aura": 0, "luck": 0, "power": 0, "level": 1, "xp": 0}
    console.print(f"[green]✅ Member {name} added![/green]")

def aura_trainer():
    name = select_member()
    if not name: return
    members[name]["aura"] += 10
    gain_xp(name, 20)
    console.print(f"[magenta]🔥 Aura increased → {members[name]['aura']}[/magenta]")

def luck_training():
    name = select_member()
    if not name: return
    members[name]["luck"] += 5
    gain_xp(name, 15)
    console.print(f"[green]🍀 Luck increased → {members[name]['luck']}[/green]")

def luck_increaser():
    name = select_member()
    if not name: return
    members[name]["luck"] += 20
    gain_xp(name, 30)
    console.print(f"[yellow]✨ Luck boosted → {members[name]['luck']}[/yellow]")

def power_training():
    name = select_member()
    if not name: return
    members[name]["power"] += 15
    gain_xp(name, 25)
    console.print(f"[blue]💪 Power increased → {members[name]['power']}[/blue]")

# ===============================
# EXTRA FEATURES (6–10)
# ===============================
def random_luck_event():
    name = select_member()
    if not name: return
    change = random.randint(-10, 30)
    members[name]["luck"] += change
    gain_xp(name, 10)
    console.print(f"[cyan]🎲 Random Luck Event: {change} → {members[name]['luck']}[/cyan]")

def rank_viewer():
    table = Table(title="🏆 HUNTRIX RANKINGS", show_lines=True)
    table.add_column("Name", style="cyan")
    table.add_column("Level", style="green")
    table.add_column("Rank", style="yellow")

    for name, s in members.items():
        lvl = s["level"]
        rank = "S" if lvl >= 10 else "A" if lvl >= 7 else "B" if lvl >= 4 else "C"
        table.add_row(name, str(lvl), rank)

    console.print(table)

def save_members():
    with open("huntrix_members.json", "w") as f:
        json.dump(members, f, indent=4)
    console.print("[green]💾 Members saved![/green]")

def load_members():
    if not os.path.exists("huntrix_members.json"):
        console.print("[red]❌ No save file found![/red]")
        return
    global members
    with open("huntrix_members.json", "r") as f:
        members = json.load(f)
    console.print("[green]📂 Members loaded![/green]")

def show_members():
    table = Table(title="📊 HUNTRIX MEMBERS STATUS", show_lines=True)
    table.add_column("Name", style="cyan")
    table.add_column("Aura 🔥")
    table.add_column("Luck 🍀")
    table.add_column("Power 💪")
    table.add_column("XP")
    table.add_column("Level 🧬")

    for n, s in members.items():
        table.add_row(
            n,
            str(s["aura"]),
            str(s["luck"]),
            str(s["power"]),
            str(s["xp"]),
            str(s["level"])
        )
    console.print(table)

# ===============================
# MENU
# ===============================
def main_menu():
    while True:
        console.print(Panel.fit(
            """[bold cyan]HUNTRIX TRAINER[/bold cyan]
1. Add Member
2. Aura Trainer
3. Luck Training
4. Luck Increaser
5. Power Training
6. Random Luck Event
7. Rank Viewer
8. Save Members
9. Load Members
10. Show Members
11. Exit""",
            border_style="bright_blue"
        ))

        choice = Prompt.ask(
            "[yellow]Choose an option[/yellow]",
            choices=[str(i) for i in range(1, 12)]
        )

        actions = {
            "1": add_member,
            "2": aura_trainer,
            "3": luck_training,
            "4": luck_increaser,
            "5": power_training,
            "6": random_luck_event,
            "7": rank_viewer,
            "8": save_members,
            "9": load_members,
            "10": show_members
        }

        if choice == "11":
            console.print("[bold green]👋 Exiting Huntrix Trainer![/bold green]")
            break

        actions[choice]()

# ===============================
# RUN
# ===============================
main_menu()
