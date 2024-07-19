import os
import sys
import time
import random
from urllib.parse import quote

from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)

# Function to clear terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ASCII art logo with color animation
logo = """
      $$$$$$$\  $$\   $$\  $$$$$$\  $$\       $$\      $$\  $$$$$$\        
      $$  __$$\ $$ |  $$ |$$  __$$\ $$ |      $$ | $\  $$ |$$  __$$\       
      $$ |  $$ |$$ |  $$ |$$ /  $$ |$$ |      $$ |$$$\ $$ |$$ /  $$ |      
      $$$$$$$\ |$$$$$$$$ |$$ |  $$ |$$ |      $$ $$ $$\$$ |$$$$$$$$ |      
      $$  __$$\ $$  __$$ |$$ |  $$ |$$ |      $$$$  _$$$$ |$$  __$$ |      
      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |      $$$  / \$$$ |$$ |  $$ |      
      $$$$$$$  |$$ |  $$ | $$$$$$  |$$$$$$$$\ $$  /   \$$ |$$ |  $$ |      
      \_______/ \__|  \__| \______/ \________|\__/     \__|\__|  \__|                                                                              
"""

# Function to print colored logo with animation
def print_colored_logo(logo):
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    for line in logo.split("\n"):
        time.sleep(0.1)
        color = random.choice(colors)
        sys.stdout.write("\033[1m")  # Bold text
        for char in line:
            sys.stdout.write(color + char)
            sys.stdout.flush()
            time.sleep(0.002)
        sys.stdout.write("\n")
        sys.stdout.flush()

# Functions for specific actions
def multi_cookies_bookmark():
    os.system('git pull')
    os.system('chmod 777 cookiesbookmark')
    os.system('./cookiesbookmark')

def multi_token_bookmark():
    os.system('git pull')
    os.system('chmod 777 tukanbookmark')
    os.system('./tukanbookmark')

def follow_owner_fb_account():
    clear_screen()
    os.system("xdg-open https://www.facebook.com/profile.php?id=100083151961248")
    input("\nPress Enter to return to the main menu...")
    main_menu()

def resume_wall():
    os.system('git pull')
    os.system('chmod 777 resume')
    os.system('./resume')

def watch_video():
    os.system("xdg-open https://youtu.be/rv8nm8DbsIg?si=jlZXrG1HUL-CEkit")

# Function for the main menu
def main_menu():
    clear_screen()
    print_colored_logo(logo)
    print("[1] Multi Cookies Bookmark")
    print("[2] Multi Token Bookmark")
    print("[3] Follow Owner Fb Account")
    print("[4] Resume Wall Loader")
    print("[5] Watch Video")
    choice = input("Enter your choice :: ")

    if choice == '1':
        multi_cookies_bookmark()
    elif choice == '2':
        multi_token_bookmark()
    elif choice == '3':
        follow_owner_fb_account()
    elif choice == '4':
        resume_wall()
    elif choice == '5':
        watch_video()
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
        input("\nPress Enter to return to the main menu...")
        main_menu()

# Run the main menu directly
main_menu()
