from rich.console import Console
import subprocess as sp
from colorama import Fore, Style, init
init(autoreset=True)  # Automatically reset styles after each print

# def print_banner():
#     """Prints a colorful banner."""
#     print(Fore.LIGHTCYAN_EX+ Style.BRIGHT)
#     print("=======================================================")
#     print("               WELCOME TO COMPANY DB TOOL              ")
#     print("=======================================================")
#     print(Style.RESET_ALL)

def print_menu():
    """Prints the main menu with colors."""
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "MAIN MENU:")
    print(Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "1." + Style.RESET_ALL + " Get warrior details")
    print(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "2." + Style.RESET_ALL + " Get Details of Divine weapon ")
    print(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "3." + Style.RESET_ALL + " Get Battle Formation Details")
    print(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "4." + Style.RESET_ALL + " Get Kinngdom Details")
    print(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "5." + Style.RESET_ALL + " Get Total Strength of Anga_nama")
    print(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "6." + Style.RESET_ALL + " Get warrior Details on partial or full name")
    print(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "7." + Style.RESET_ALL + " Get list of divine weapon with warrior based on kingdom")
    print(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "8." + Style.RESET_ALL + " Get formation name and warrior Id based on kingdom name")
    print(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "9." + Style.RESET_ALL + " Add a new warrior")
    print(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "10." + Style.RESET_ALL + " Modify a Battle formation based on Day and army_id")
    print(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "11." + Style.RESET_ALL + " Delete Event from Yuddhahani")
    print(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "12." + Style.RESET_ALL + " Add a new Battle formation")
    print(Fore.LIGHTRED_EX+ Style.BRIGHT + "14." + Style.RESET_ALL + " Logout")
    print(Fore.LIGHTCYAN_EX+ Style.BRIGHT + "-" * 50 + Style.RESET_ALL)
