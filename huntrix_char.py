from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax

# Initialize Rich Console
console = Console()


def create_character_code():
    """Main function to generate Huntrix character code."""
    while True:
        # Display a welcome message
        console.print(Panel(
            "[bold cyan]Enter the details for a new Huntrix member.[/bold cyan]
A Python dictionary will be generated for you.",
            title="[bold yellow]Huntrix Character Code Generator[/bold yellow]",
            border_style="magenta"
        ))

        # --- Get Character Details from User Input ---
        name = Prompt.ask("[bold]Enter character's name[/bold]").strip()
        
        # Get and validate age
        while True:
            try:
                age = int(Prompt.ask("[bold]Enter character's age[/bold]"))
                break
            except ValueError:
                console.print("[bold red]Invalid input. Please enter a number for the age.[/bold red]")

        role = Prompt.ask("[bold]Enter character's role (e.g., Leader, Vocalist, Shadowmancer)[/bold]").strip()
        ability = Prompt.ask("[bold]Enter character's primary demon-hunting ability[/bold]").strip()

        # --- Generate Python Code ---
        code_string = f"""
'{name}': {{
    'age': {age},
    'role': '{role}',
    'ability': '{ability}',
    'group': 'Huntrix'
}}
"""
        
        # --- Display the Generated Code ---
        console.print(Panel(
            Syntax(code_string, "python", theme="solarized-dark", line_numbers=True),
            title="[bold green]Generated Python Code[/bold green]",
            border_style="green"
        ))

        # --- Ask to Continue or Exit ---
        play_again = Prompt.ask("
[bold]Do you want to create another character?[/bold]", choices=["yes", "no"], default="yes")
        if play_again.lower() != 'yes':
            console.print("[bold yellow]Generator closed. Happy coding![/bold yellow]")
            break
        console.clear()

if __name__ == "__main__":
    create_character_code()
