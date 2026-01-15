import time
import random
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.console import Console
from rich.layout import Layout
from rich.progress import Progress, BarColumn, TextColumn

console = Console()

def generate_rate_table(rate_value, status):
    """Generates the data table for the terminal."""
    table = Table(title="[bold cyan]HUNTRIX SYSTEM MONITOR[/bold cyan]")
    table.add_column("Metric", style="magenta")
    table.add_column("Value", justify="right", style="green")
    
    table.add_row("Current Detection Rate", f"{rate_value:.2f} req/s")
    table.add_row("System Integrity", f"{random.randint(95, 100)}%")
    table.add_row("Status", status)
    return table

def run_terminal():
    # Setup the layout
    layout = Layout()
    layout.split_column(
        Layout(name="upper"),
        Layout(name="lower")
    )

    with Live(layout, refresh_per_second=4) as live:
        current_rate = 10.5
        
        for _ in range(100):
            # Simulate rate fluctuations
            current_rate += random.uniform(-0.5, 0.6)
            status = "[bold green]ACTIVE[/bold green]" if current_rate > 5 else "[bold red]LOW[/bold red]"
            
            # Update the Top Panel (Table)
            layout["upper"].update(
                Panel(generate_rate_table(current_rate, status), border_style="blue")
            )
            
            # Update the Bottom Panel (Log simulation)
            layout["lower"].update(
                Panel(f"[grey]LOG:[/grey] Scanning sector {random.randint(100, 999)}... "
                      f"Detection at {current_rate:.1f}", 
                      title="System Logs", border_style="white")
            )
            
            time.sleep(0.5)

if __name__ == "__main__":
    try:
        run_terminal()
    except KeyboardInterrupt:
        console.print("\n[bold red]Terminal Terminated.[/bold red]")

