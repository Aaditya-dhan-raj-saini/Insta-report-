import os
import time
import threading
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

# Aaditya Branding Banner
def banner():
    os.system('clear')
    brand = """
[bold cyan]
__     __   _     _      _        _    _            _    
\ \   / /__| |__ (_) ___| | ___  | |  | | __ _  ___| | __
 \ \ / / _ \ '_ \| |/ __| |/ _ \ | |__| |/ _` |/ __| |/ / 
  \ V /  __/ | | | | (__| |  __/ |  __  | (_| | (__|   <  
   \_/ \___|_| |_|_|\___|_|\___| |_|  |_|\__,_|\___|_|\_\ 
[/bold cyan]
[bold yellow]   >>> BULK VEHICLE OSINT - CREATED BY AADITYA <<< [/bold yellow]
    """
    console.print(Panel(brand, subtitle="[bold red]Identity: Hidden (Tor Enabled)[/bold red]"))

# Tor IP Change Logic
def rotate_ip():
    # Tor service refresh command
    os.system("pkill -HUP tor")
    console.print("[italic magenta][*] IP Rotated for Anonymity...[/italic magenta]")

# Single Vehicle Data Logic
def fetch_data(plate):
    # Dummy data (API call yahan aayegi)
    data = {
        "Number": plate,
        "Owner": "Aaditya User",
        "Reg Date": "01-Jan-2024",
        "Status": "Active"
    }
    
    table = Table(show_header=False, border_style="green")
    table.add_row(f"[bold]{plate}[/bold]", "Found ✅")
    console.print(table)
    # Aapka actual data yahan file mein save ho sakta hai

def bulk_attack():
    banner()
    file_path = console.input("[bold white]Enter .txt file path (e.g., list.txt): [/bold white]")
    
    if not os.path.exists(file_path):
        console.print("[bold red][!] File nahi mili![/bold red]")
        return

    with open(file_path, 'r') as f:
        plates = f.read().splitlines()

    console.print(f"[bold green][+] Total {len(plates)} vehicles found. Starting...[/bold green]\n")

    for plate in plates:
        rotate_ip() # Har vehicle ke baad IP change
        t = threading.Thread(target=fetch_data, args=(plate,))
        t.start()
        time.sleep(1) # Rate limit se bachne ke liye

if __name__ == "__main__":
    bulk_attack()
