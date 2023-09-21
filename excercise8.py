from rich.table import Table
from rich.console import Console
console = Console()
dogs = Table("To do list:")
dogs.add_column("Name") # tabllen rensas on vi lägger till kolumner
dogs.add_column("Breed") # tabllen rensas on vi lägger till kolumner
dogs.add_column("Age") # tabllen rensas on vi lägger till kolumner

dogs.add_row("1","Fido","poodle","3")
dogs.add_row("1","Silk","great dane","2")
dogs.add_row("1","Fido","poodle","3")
console.print(dogs)


# Create a table with column headers
table = Table(title="Sample Table")
table.add_column("Name", style="bold cyan")
table.add_column("Age", style="bold magenta")
table.add_column("Country", style="bold yellow")

# Add rows to the table
table.add_row("Alice", "28", "USA")
table.add_row("Bob", "32", "Canada")
table.add_row("Charlie", "22", "UK")

# Print the table using the rich console
console.print(table)