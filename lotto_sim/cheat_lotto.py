# file for simulating playing the lottery (but cheating)!

# import rich functions and classes
from math import comb
from rich.console import Console
from rich.panel import Panel
from datetime import datetime
import time
import csv
import random

console = Console()

def cheat_lotto(attempt, chosen_numbers, game_won, num_drawn, lowest_value, highest_value, winning_numbers):
    """
    Simulates playing a lottery (after reading JSON configruation file) but cheats
    """

    console.print("[italic yellow]This will now 'cheat' at playing the lottery.[/italic yellow]")


    with console.status("[green]Now playing, please wait...[/green]") as status:
        # additional settings
        combinations = []
        # fill the correct number of combinations with blanks
        correct_combination = []
        while len(correct_combination) < num_drawn:
            correct_combination.append('_')

        date = datetime.now().strftime('%u%d%G')
        current_time = datetime.now().strftime("%H-%M-%S")
        # start timer
        start = time.perf_counter()
        # game loops while the winning numbers aren't drawn
        while game_won == False:
            while len(chosen_numbers) < num_drawn:
                # pick a random number between the set lowest and highest value
                chosen_numbers.append(random.randint(lowest_value, highest_value))
            if chosen_numbers == winning_numbers or correct_combination == winning_numbers:
                combinations.append(chosen_numbers)
                # end timer
                end = time.perf_counter()
                # write all combinations to a csv file
                with open(f'combinations_{date}_{current_time}.csv', "w") as file:
                    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    for x in combinations:
                        writer.writerow(x)
                # print results to console
                console.print(Panel.fit("🎉CONGRATULATIONS! YOU WON!🎉", style="bold green"))
                console.print(f"[italic yellow]It only took {attempt} attempts!\nIt took a total of {end - start:0.4f} seconds![/italic yellow]")
                game_won = True
            else:
                # compare the selected numbers with the winning numbers and look for matches
                for x in chosen_numbers:
                    for y in winning_numbers:
                        if x == y:
                            correct_combination[winning_numbers.index(y)] = x
                # take combination and append
                combinations.append(chosen_numbers.copy())
                # clear list for next pick
                chosen_numbers.clear()
                # increment
                attempt += 1
