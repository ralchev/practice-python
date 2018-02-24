#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays
(using input), compare them, print out a message of congratulations to the
winner, and ask if the players want to start a new game)
"""

player1 = str(input("Who is player 1?"))
player2 = str(input("Who is player 2?"))

def move():
    player1_move = str(input(player1 + ", what do you choose -- rock, paper or scissors?"))
    player2_move = str(input(player2 + ", and you? Rock, paper or scissors?"))

    if player1_move == player2_move:
        print("Equal game!")
    elif player1_move == "rock":
        if player2_move == "paper":
            print(player2 + ", you win!")
        else:
            print(player1 + ", you win!")
    elif player1_move == "scissors":
        if player2_move == "rock":
            print(player2 + ", you win!")
        else:
            print(player1 + ", you win!")
    elif player1_move == "paper":
        if player2_move == "scissors":
            print(player2 + ", you win!")
        else:
            print(player1 + ", you win!")
    
    another_game = input("Want to play again? Yes or no?")
    if another_game == "yes":
        move()
    else:
        print("That was all, folks!")

move()