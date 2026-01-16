import time
import random
from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from rich.prompt import Prompt
from rich.align import Align

console = Console()

def start_trainer():
    console.clear()
    console.print(Panel.fit(
        "[bold magenta]✦ HUNTRIX AURA TRAINER v1.1 ✦[/bold magenta]\n"
        "[cyan]Coding Prowess + Destiny Alignment[/cyan]",
        border_style="bold blue"
    ))

    # --- PHASE 1: CODING CHALLENGE ---
    console.print("\n[bold white]> Phase 1: Coding Challenge[/bold white]")
    q1 = Prompt.ask(
        "In Python, which symbol is used for comments?",
        choices=["//", "#", "/*"],
        default="#"
    )
    
    coding_score = 0
    if q1 == "#":
        console.print("[green]Correct! Coding Skill +50[/green]")
        coding_score = 50
    else:
        console.print("[red]Incorrect. Coding Skill +10[/red]")
        coding_score = 10

    # --- PHASE 2: LUCK TRAINING ---
    console.print("\n[bold white]> Phase 2: Luck Training[/bold white]")
    # Using the corrected 'track' function here
    for _ in track(range(10), description="Channelling Spirit Energy..."):
        time.sleep(0.1)
    
    luck_factor = random.randint(1, 100)
    
    # --- PHASE 3: MEMBER BLESSING (NEW!) ---
    members = ["Rumi", "Mira", "Zoey"]
    blesser = random.choice(members)
    multiplier = round(random.uniform(1.1, 1.5), 2)
    
    console.print(f"\n[bold magenta]✨ {blesser} has granted you a blessing! (x{multiplier} Aura)[/bold magenta]")

    # --- FINAL CALCULATION ---
    base_aura = (coding_score * 5) + luck_factor
    final_aura = int(base_aura * multiplier)
    
    # Ranking Logic
    if final_aura > 450:
        rank = "[bold reverse magenta] S-TIER HUNTER [/bold reverse magenta]"
    elif final_aura > 250:
        rank = "[bold cyan] ELITE CODER [/bold cyan]"
    else:
        rank = "[bold white] TRAINEE [/bold white]"

    result_panel = Panel(
        Align.center(
            f"Base Skill: {coding_score}\n"
            f"Luck Roll: {luck_factor}\n"
            f"Blessing: {blesser} ({multiplier}x)\n\n"
            f"[bold yellow]TOTAL AURA: {final_aura}[/bold yellow]\n"
            f"RANK: {rank}"
        ),
        title="[bold green]TRAINING COMPLETE[/bold green]",
        border_style="bright_magenta"
    )
    
    console.print("\n", result_panel)

if __name__ == "__main__":
    try:
        start_trainer()
    except KeyboardInterrupt:
        console.print("\n[red]Training interrupted. Aura lost![/red]")

