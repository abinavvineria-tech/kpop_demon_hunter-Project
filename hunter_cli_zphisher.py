# import click
import time
import sys


def loading_animation():
    """
    Displays a simple loading bar animation.
    """
    click.echo("Initializing...")
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]",
                 "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for frame in animation:
        sys.stdout.write(f"\\r{frame} Loading...")
        sys.stdout.flush()
        time.sleep(0.2)

    sys.stdout.write("\\r" + " " * 20 + "\\r")  # Clears the line
    click.secho("Initialization Complete!", fg="green", bold=True)
    time.sleep(1)
    click.clear()


@click.command()
@click.option("-n", "--name", prompt=True, help="The name of the Huntrix.")
@click.option("-a", "--age", prompt=True, type=int, help="The age of the Huntrix.")
@click.option("-c", "--country", prompt=True, help="The country of origin for the Huntrix.")
def create_hunter_profile(name, age, country):
    """
    A modern CLI tool with a Zphisher-like interface for creating K-pop Demon Hunter profiles.
    """
    loading_animation()

    # Zphisher-style banner
    banner = [
        "██╗  ██╗██╗   ██╗██████╗ ██████╗ ",
        "██║  ██║██║   ██║██╔══██╗██╔══██╗",
        "███████║██║   ██║██████╔╝██████╔╝",
        "██╔══██║██║   ██║██╔═══╝ ██╔═══╝ ",
        "██║  ██║╚██████╔╝██║     ██║     ",
        "╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝     ",
    ]

    for line in banner:
        click.secho(line, fg="magenta", bold=True)
        time.sleep(0.05)  # Adds a quick animation effect

    click.secho("\
         < A K-POP DEMON HUNTER CREATION TOOL >", fg="cyan")
    click.echo()

    # Display profile with styled output
    click.secho("[+] Profile Details:", fg="yellow", bold=True)
    click.secho("====================", fg="yellow")
    click.secho(f"  [>] Name:    {name}", fg="white")
    click.secho(f"  [>] Age:     {age}", fg="white")
    click.secho(f"  [>] Country: {country}", fg="white")
    click.secho("====================", fg="yellow")
    click.echo()
    click.secho("Profile created successfully!", fg="green", bold=True)


if __name__ == "__main__":
    create_hunter_profile()]
