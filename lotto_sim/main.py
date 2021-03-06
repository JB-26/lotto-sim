# import rich functions and classes
from rich.console import Console
from rich.panel import Panel

#import other functions
from set_numbers import set_numbers
from play_lotto import play_lotto

# new console object
console = Console()


def main():
    """
    Main function
    """
    
    while True:
        console.print(Panel.fit("Welcome to Lotto Sim!", style="bold cyan"))
        console.print(Panel.fit("[italic yellow]Please type the letters that are highlighted in green to access the functions[/italic yellow]\n[bold green]S[/bold green]et numbers\n[bold green]P[/bold green]lay lottery\n[bold green]Q[/bold green]uit", title="Lotto - Menu 🔮", subtitle="By Joshua Blewitt"))

        console.print("[green]Enter your choice[/green]")
        choice = input().upper()

        if choice == 'S':
            set_numbers()
        elif choice == 'P':
            play_lotto()
        elif choice == 'Q':
            console.print("Goodbye!")
            break
        else:
            console.print("[bold red]Your command was invalid! Please try again![/bold red]")


if __name__ == "__main__":
    main()