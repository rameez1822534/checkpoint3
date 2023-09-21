from rich.tree import Tree
from rich.console import Console

console = Console()

group1 = Tree("[red] Groupp1")
group1.add("Johan")
group1.add("Ahmad")
group1.add("habib")


group2 = Tree("[green]Grupp2")
group2.add("Ali")
group2.add("Khaqan")
group2.add("Zara")
# console.print(group2)

groups = Tree("[blue] Grupper")
groups.add(group1)
groups.add(group2)

console.print(groups)