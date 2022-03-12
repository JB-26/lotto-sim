# file for setting numbers drawn from the lottery

# import rich functions and classes
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# reading and writing json files
import json

# new console object
console = Console()
# new table object
table = Table(title="Game information")
table.add_column("Field", justify="center")
table.add_column("Value", justify="center")

def set_numbers():
    """
    Function for setting numbers
    """
    console.print(Panel.fit("Set numbers", style="bold cyan"))
    console.print("[green]Step 1: Configure[/green]")
    while True:
        try:
            console.print("Please enter how many numbers are drawn")
            num_drawn = int(input())
            break
        except:
            console.print("[bold red]ERROR![/bold red] Please try again")

    while True:
        try:
            console.print("Please enter the [bold]lowest[bold] value that the lottery game will accept")
            lowest_value = int(input())
            break
        except:
            console.print("[bold red]ERROR![/bold red] Please try again")

    while True:
        try:
            console.print("Please enter the [bold]highest[bold] value that the lottery game will accept")
            highest_value = int(input())
            break
        except:
            console.print("[bold red]ERROR![/bold red] Please try again")

    # add rows to the table
    table.add_row("Number of drawn numbers", str(num_drawn))
    table.add_row("Lowest number value", str(lowest_value))
    table.add_row("Highest number value", str(highest_value))

    console.print(table)

    console.print("Press enter to continue")
    enter = input()

    console.print("[green]Step 2: Winning numbers[/green]")
    console.print("Enter the winning numbers for the lottery")

    # list of winning numbers
    winning_list = []
    add_count = 1

    while add_count <= num_drawn:
        try:
            console.print(f"Enter a winning number that is between {lowest_value} and {highest_value}")
            drawn_number = int(input())
            # check if number is between the lowest and highest value
            if drawn_number >= lowest_value and drawn_number <= highest_value:
                winning_list.append(drawn_number)
                add_count += 1
            else:
                console.print("[bold red]ERROR![/bold red] Please try again")
        except:
            console.print("[bold red]ERROR![/bold red] Please try again")
    
    console.print("The winning numbers are:")
    console.print(winning_list)

    console.print("Now writing the game information and numbers to a JSON file...")

    # creating dictionary to be exported as a JSON file
    config_dict = {
        "drawn" : num_drawn,
        "lowest": lowest_value,
        "highest": highest_value,
        "numbers": winning_list
    }

    # serialising JSON
    json_object = json.dumps(config_dict, indent=4)

    # write JSON to a file
    with open("lotto_game.json", "w") as game_file:
        game_file.write(json_object)
    