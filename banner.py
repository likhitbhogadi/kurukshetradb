from rich.console import Console
from rich.panel import Panel

console = Console()


def print_banner():
    """Display a colorful banner with Rich."""
    banner = """
  K   K   U   U  RRRRR   U   U  K   K  SSSSS   H   H  EEEEE  TTTTT  RRRRR    AAAAA  
  K  K    U   U  R   R   U   U  K  K   S       H   H  E        T    R   R   A     A 
  KKK     U   U  RRRRR   U   U  KKK    SSSSS   HHHHH  EEEE     T    RRRRR   AAAAAAA
  K  K    U   U  R  R    U   U  K  K       S   H   H  E        T    R  R    A     A 
  K   K    UUU   R   R    UUU   K   K  SSSSS   H   H  EEEEE    T    R   R   A     A
"""

    console.print(Panel(banner, title="[bold bright_red]WELCOME TO KURUKSHETRA DB TOOL[/bold bright_red]", style="bold bright_yellow"))
