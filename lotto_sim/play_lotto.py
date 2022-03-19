# file for simulating playing the lottery!

# import rich functions and classes
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# import picking numbers function
from pick_numbers import pick_numbers
# import cheat function
from cheat_lotto import cheat_lotto

# reading json files
import json

# new console object
console = Console()

# variables for playing
attempt = 1
chosen_numbers = []
game_won = False

def play_lotto():
    """
    Simulates playing a lottery (after reading JSON configruation file)
    """
    
    # new table object
    table = Table(title="Game information")
    table.add_column("Field", justify="center")
    table.add_column("Value", justify="center")
    
    console.print(Panel.fit("Play lottery", style="bold cyan"))

    try:
        # display animation to show user that the JSON file is being read
        with console.status("[purple]Reading game information from JSON...[/purple]") as status:
            with open('lotto_game.json', 'r') as read_file:
                data = json.load(read_file)
        
        console.print("[bold green]Success! Found game JSON file! :clap:[/bold green]")

        # assign variables to JSON values
        num_drawn = data['drawn']
        lowest_value = data['lowest']
        highest_value = data['highest']
        winning_numbers = data['numbers']

        # add rows to the table
        table.add_row("Number of drawn numbers", str(num_drawn))
        table.add_row("Lowest number value", str(lowest_value))
        table.add_row("Highest number value", str(highest_value))
        table.add_row("Winning numbers", str(winning_numbers))

        console.print(table)

        console.print("[bold yellow]Let's play![/bold yellow]")

        console.print("[italic]Would you want to play the lottery by letting the program send random numbers or cheat?\nEnter '1' for normal play or '2' for cheat play[/italic]")

        choice = int(input())

        if choice == 1:
            console.print("[bold red]Warning![/bold red] This will take a long time to do and may take up significant resources on your computer!")
            console.print("[italic]Press enter to play[/italic]")
            enter = input()
            pick_numbers(attempt, chosen_numbers, game_won, num_drawn, lowest_value, highest_value, winning_numbers)
        elif choice == 2:
            console.print("[bold red]Warning![/bold red] This will take a long time to do and may take up significant resources on your computer!")
            console.print("[italic]Press enter to play[/italic]")
            enter = input()
            cheat_lotto(attempt, chosen_numbers, game_won, num_drawn, lowest_value, highest_value, winning_numbers)

    except FileNotFoundError:
        console.print("[bold red]ERROR![/bold red] No JSON file found! Please configure the lottery game before playing!")

    except ValueError:
        console.print("[bold red]ERROR![/bold red] Please enter a number!")

    except:
        console.print("[bold red]ERROR![/bold red] Please try again!")
