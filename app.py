import random
import sys
import time
import os

from termcolor import colored
from pyfiglet import Figlet
from colorama import init

init()

os.system('cls' if os.name == 'nt' else 'clear')

f = Figlet(font='slant')

print(colored(f.renderText('Rock Paper Scissors'), 'cyan'))
time.sleep(1)

print(colored('Welcome to the Rock, Paper, Scissors game!', 'green'))
time.sleep(1)

print(colored('You will be playing against the computer.', 'green'))
time.sleep(1)

print(colored('The rules are simple:', 'yellow'))
time.sleep(1)

print(colored('Rock beats Scissors', 'yellow'))
print(colored('Scissors beats Paper', 'yellow'))
print(colored('Paper beats Rock', 'yellow'))
time.sleep(1)

print(colored('Let\'s start the game!', 'green'))
time.sleep(1)

options = ['rock', 'paper', 'scissors']

player_score = 0

computer_score = 0

while True:
    player_choice = input(colored('Enter your choice (rock, paper, scissors): ', 'cyan')).lower()
    if player_choice not in options:
        print(colored('Invalid choice. Please try again.', 'red'))
        continue
    computer_choice = random.choice(options)
    print(colored(f'Computer chose: {computer_choice}', 'magenta'))
    if player_choice == computer_choice:
        print(colored('It\'s a tie!', 'yellow'))
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        print(colored('You win this round!', 'green'))
        player_score += 1
    else:
        print(colored('Computer wins this round!', 'red'))
        computer_score += 1
    print(colored(f'Score - You: {player_score} | Computer: {computer_score}', 'blue'))
    play_again = input(colored('Do you want to play again? (yes/no): ', 'cyan')).lower()
    if play_again != 'yes':
        print(colored('Thanks for playing! Final Score:', 'green'))
        print(colored(f'You: {player_score} | Computer: {computer_score}', 'blue'))
        sys.exit()
