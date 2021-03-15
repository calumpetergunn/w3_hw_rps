import random

class Game():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

def find_winner(player1, player2):
    if player1.player_choice == player2.player_choice:
        return "It's a draw!"
    elif player1.player_choice == "rock":
        if player2.player_choice == "scissors":
            return player1.player_name + " wins with " + player1.player_choice
        else:
            return player2.player_name + " wins with " + player2.player_choice
    elif player1.player_choice == "paper":
        if player2.player_choice == "rock":
            return player1.player_name + " wins with " + player1.player_choice
        else:
            return player2.player_name + " wins with " + player2.player_choice
    elif player1.player_choice == "scissors":
        if player2.player_choice == "paper":
            return player1.player_name + " wins with " + player1.player_choice
        else:
            return player2.player_name + " wins with " + player2.player_choice

def computer_result():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


   
