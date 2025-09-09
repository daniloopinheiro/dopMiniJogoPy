from django.shortcuts import render
import random

def game_view(request):
    options = ['rock', 'paper', 'scissors']
    player_choice = request.GET.get('choice', '').lower()
    computer_choice = random.choice(options)
    result = ""

    if player_choice not in options and player_choice != "":
        result = "Invalid choice. Please try again."
    elif player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        result = "You win this round!"
    elif player_choice:
        result = "Computer wins this round!"

    context = {
        'player_choice': player_choice,
        'computer_choice': computer_choice,
        'result': result,
    }
    return render(request, 'game/game.html', context)
