from rich.console import Console

console = Console()

# print([1 , 2 , 3])
# console.print([1 , 2 , 3])

# console.print("[blue underline]ser ut som en länk")
# console.print("[bold]Fetstil[/bold] [italic]Kursiv[/italic]")
# console.print("Vit text på blå bakgrund" , style="white on blue")

# console.log("När vi använder log får vi också en tidpunkt")
# console.rule("[bold red] Rubrik til ny avdelning")


# from rich.progress import track #progressbar
# import time #för progressbar

# for n in track(range(10), description="Processing..."):
#     # gör arbete här
#     time.sleep(1) # Bara vänta en sekund 

# from rich.tree import Tree

# group1 = Tree("[red] Groupp1")
# group1.add("Johan")
# group1.add("Ahmad")
# group1.add("habib")


# group2 = Tree("[green]Grupp2")
# group2.add("Ali")
# group2.add("Khaqan")
# group2.add("Zara")
# # console.print(group2)

# groups = Tree("[blue] Grupper")
# groups.add(group1)
# groups.add(group2)

# console.print(groups)


# from rich.table import Table

# todo = Table("to do list")

# todo.add_column("Check") # tabllen rensas on vi lägger till kolumner
# todo.add_row ("[red]Make coffee", "❤️")
# todo.add_row ("[green]Drink coffee", "👍")
# todo.add_row ("Enjoy coffee", "👌")

# console.print(todo)

# console.print( "a [yellow]Warning")
# console.print( "an [red]Error")
# console.print( "and [green]Success")


#excercise 2
# from rich import print
# from rich.console import Console

# # Initialize the console
# console = Console()

# # List of available colors
# colors = [("black"),
#     ("red"),
#     ("green"),
#     # ... (other colors from your list)
#     ("grey84"),
#     ("light_steel_blue1"),
#     ("yellow1"),
#     ("dark_olive_green1"),
#     ("honeydew2"),
#     ("light_cyan1"),
#     ("red1")
# ]


# # Word to print
# word = "Hello"

# # Print the word in each color
# for color in colors:
#     styled_word = f"[{color}]{word}[/{color}]"
#     console.print(styled_word)

#excercise3
#This text is bold, this text is italic and this text is underlined

# console.print("This text is [bold]bold[/bold], this text is [italic]italic[/italic] and this text is [underline]underlined[/underline]")


#excercsie 4 
#console.print("Visit [blue][link=https://rich.readthedocs.io/en/stable/style.html#style-class]Rich class[/link]!")

#excercise 5
# import random 

# sec_no = random.randint(1, 100)
# for n in range(1, 101):
#     no = []
#     n += 1 
import random
from rich import print
from rich.prompt import IntPrompt, Confirm

def no_guessing():
    while True:
        secret_number  = random.randint(1 , 100)
        attempts = 0
        print("Welcome to the Guess the Number game!")
        print("I've selected a random number between 1 and 100. Try to guess it!")
        while True:
            attempts += 1
            guess = IntPrompt.ask("Enter your guess: ")

            if guess == secret_number:
                print("[bold green]Congratulations[/bold green] you have guess the right number")
                play_again = Confirm.ask("Do you want to play again [bold green](y/n)[/bold green]")
                if not play_again:
                    print("Thanks for playing")
                    break
                elif guess < secret_number:
                    print("[bold yellow]Try a higher number.[/bold yellow]")
            else:
                print("[bold yellow]Try a lower number.[/bold yellow]")

if __name__ == "__main__":
    no_guessing()






