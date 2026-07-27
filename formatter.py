from rich.console import Console

console = Console()


def success(message: str):
    console.print(f"[green]{message}[/green]")


def error(message: str):
    console.print(f"[red]{message}[/red]")