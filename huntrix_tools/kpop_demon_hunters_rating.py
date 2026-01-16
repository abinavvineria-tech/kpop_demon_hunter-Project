import time
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns
from rich.progress import BarColumn, Progress, TextColumn

console = Console()

def get_star_rating(score):
    """Converts a 1-5 score into emoji stars."""
    return "⭐" * score + "ᛜ" * (5 - score)

def create_hunter_card(name, role, stats):
    """Creates a visual card for a specific hunter."""
    rating_text = (
        f"[bold yellow]Rank:[/bold yellow] {stats['rank']}\n"
        f"[bold magenta]Vocals:[/bold magenta] {get_star_rating(stats['vocals'])}\n"
        f"[bold cyan]Dance:[/bold cyan]  {get_star_rating(stats['dance'])}\n"
        f"[bold red]Combat:[/bold red] {get_star_rating(stats['combat'])}\n"
        f"---"
    )
    return Panel(rating_text, title=f"[bold white]{name}[/bold white]", subtitle=f"[italic]{role}[/italic]", expand=False)

# Data for the Huntrix/Saja universe
hunters = {
    "Rumi": {"rank": "S-Tier", "vocals": 5, "dance": 4, "combat": 5},
    "Mira": {"rank": "A-Tier", "vocals": 3, "dance": 5, "combat": 4},
    "Zoey": {"rank": "S-Tier", "vocals": 4, "dance": 4, "combat": 3},
}

def display_ratings():
    console.print("\n[bold reverse magenta]  ✦ HUNTRIX MISSION CONTROL: HUNTER RATINGS ✦  [/bold reverse magenta]\n")
    
    # 1. Display Individual Cards
    cards = [create_hunter_card(name, "Demon Hunter", stats) for name, stats in hunters.items()]
    console.print(Columns(cards))

    # 2. Display a Comparison Table
    table = Table(title="Live Squad Performance Metrics", border_style="bright_blue")
    table.add_column("Hunter", style="cyan", no_wrap=True)
    table.add_column("Exorcisms", justify="right", style="red")
    table.add_column("Fan Support", justify="right", style="green")
    table.add_column("Spirit Energy", justify="right", style="yellow")

    table.add_row("Rumi", "142", "98%", "MAX")
    table.add_row("Mira", "89", "92%", "85%")
    table.add_row("Zoey", "114", "99%", "92%")

    console.print(table)

    # 3. Simulate a "Loading" Power Level
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=40, style="magenta"),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    ) as progress:
        task = progress.add_task("[bold white]Syncing Squad Resonance...", total=100)
        while not progress.finished:
            progress.update(task, advance=0.5)
            time.sleep(0.02)

if __name__ == "__main__":
    display_ratings()

