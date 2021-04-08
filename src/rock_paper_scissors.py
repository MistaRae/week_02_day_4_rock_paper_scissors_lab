# import unittest ???
from src.player_class import Player


def play_game(player1, player2):
    if player1.gesture == player2.gesture:
        return "It's a draw!"
    if player1.gesture == "rock" and player2.gesture == "scissors":
        return "Rock wins!"
    if player1.gesture == "rock" and player2.gesture == "paper":
        return "Paper wins!"
    if player1.gesture == "rock" and player2.gesture == "Spock":
        return "Spock wins!"
    if player1.gesture == "rock" and player2.gesture == "lizard":
        return "Rock wins!"

    if player1.gesture == "scissors" and player2.gesture == "paper":
        return "Scissors wins!"
    if player1.gesture == "scissors" and player2.gesture == "rock":
        return "Rock wins!"
    if player1.gesture == "scissors" and player2.gesture == "Spock":
        return "Spock wins!"
    if player1.gesture == "scissors" and player2.gesture == "lizard":
        return "Scissors wins!"

    if player1.gesture == "paper" and player2.gesture == "Spock":
        return "Paper wins!"
    if player1.gesture == "paper" and player2.gesture == "lizard":
        return "Lizard wins!"
    if player1.gesture == "paper" and player2.gesture == "rock":
        return "Paper wins!"
    if player1.gesture == "paper" and player2.gesture == "scissors":
        return "Scissors wins!"

    if player1.gesture == "lizard" and player2.gesture == "rock":
        return "Rock wins!"
    if player1.gesture == "lizard" and player2.gesture == "scissors":
        return "Scissors wins!"
    if player1.gesture == "lizard" and player2.gesture == "Spock":
        return "Lizard wins!"
    if player1.gesture == "lizard" and player2.gesture == "paper":
        return "Lizard wins!"

    if player1.gesture == "Spock" and player2.gesture == "paper":
        return "Paper wins!"
    if player1.gesture == "Spock" and player2.gesture == "rock":
        return "Spock wins!"
    if player1.gesture == "Spock" and player2.gesture == "scissors":
        return "Spock wins!"
    if player1.gesture == "Spock" and player2.gesture == "lizard":
        return "Lizard wins!"