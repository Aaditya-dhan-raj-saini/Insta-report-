from rich.console import Console
from rich.table import Table

console = Console()

def show_results(user, status):
    table = Table(show_header=True, header_style="bold green")
    table.add_column("Target Username", style="dim")
    table.add_column("Status")
    table.add_column("Network")

    table.add_row(user, status, "Tor/Encrypted")
    console.print(table)
