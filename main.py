import click
import platform
import psutil

@click.group()
def cli():
    """Huntrix Multi-Tool: Your Swiss Army Knife in Python."""
    pass

@cli.command()
@click.argument('filename')
def read_file(filename):
    """Read contents of a file."""
    try:
        with open(filename, 'r') as f:
            click.echo(f.read())
    except FileNotFoundError:
        click.echo("File not found.")

@cli.command()
@click.argument('filename')
@click.argument('content')
def write_file(filename, content):
    """Write content to a file."""
    with open(filename, 'w') as f:
        f.write(content)
    click.echo("File written.")

@cli.command()
@click.argument('num1', type=float)
@click.argument('num2', type=float)
@click.argument('operation')
def calc(num1, num2, operation):
    """Simple calculator: add, sub, mul, div."""
    if operation == 'add':
        result = num1 + num2
    elif operation == 'sub':
        result = num1 - num2
    elif operation == 'mul':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
    else:
        result = "Invalid operation"
    click.echo(f"Result: {result}")

@cli.command()
def sysinfo():
    """Show system information."""
    click.echo(f"OS: {platform.system()} {platform.release()}")
    click.echo(f"CPU: {psutil.cpu_percent()}%")
    click.echo(f"Memory: {psutil.virtual_memory().percent}%")

if __name__ == '__main__':
    cli()
