# file for picking random numbers

# import rich functions and classes
from rich.console import Console
from rich.panel import Panel

# needed for picking random numbers
import random

console = Console()

def pick_numbers(attempt, chosen_numbers, game_won, num_drawn, lowest_value, highest_value, winning_numbers):
    """
    Picks numbers and compares to drawn numbers
    """

    with console.status("[green]Now playing, please wait...[/green]") as status:
        while game_won == False:
            while len(chosen_numbers) < num_drawn:
                chosen_numbers.append(random.randint(lowest_value, highest_value))
            if chosen_numbers == winning_numbers:
                console.print(Panel.fit("🎉CONGRATULATIONS! YOU WON!🎉", style="bold green"))
                console.print(f"[italic yellow]It only took {attempt} attempts![/italic yellow]")
                game_won = True
            else:
                chosen_numbers.clear()
                attempt += 1
