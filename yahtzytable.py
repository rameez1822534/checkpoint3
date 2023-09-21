from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Sample Table" , style="bright_white on black")
table.add_column("Upper Selection", style="bold cyan")
table.add_column("How to score", style="bold magenta")
table.add_column("Game 1 ", style="bold yellow")
table.add_column("Game 2 ", style="bold yellow")


table.add_row("ACES 🎲", "Count and Add only Aces", " ", " ")
table.add_row("TWOS 🎲", "Count and Add only Twos", " ", " ")
table.add_row("ACES 🎲", "Count and Add only Threes", " ", " ")
table.add_row("ACES 🎲", "Count and Add only Fours", " ", " ")
table.add_row("ACES 🎲", "Count and Add only Fives", " ", " ")
table.add_row("ACES 🎲", "Count and Add only Sixs", " ", " ")
table.add_row("Total Score", " ", " ", " ")
table.add_row("Bonus if total score is 63 or more", "Score 35", " ", " ")

# table.add_separator()

console.print(table)