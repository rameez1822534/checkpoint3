#excercise 5
# import random 


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






